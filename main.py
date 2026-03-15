import numpy as np
import pandas as pd
from ALdakerMiniNN import NeuralNetwork
from ALdakerMiniNN.layers.dense import Dense
from ALdakerMiniNN.layers.activations import ReLU, Sigmoid
from ALdakerMiniNN.layers.batchnorm import BatchNorm1D
from ALdakerMiniNN.layers.losses import BinaryCrossEntropy
from ALdakerMiniNN.optim.momentum import Momentum
from data_utils import StockDataset
from ALdakerMiniNN.layers.dropout import Dropout
import matplotlib.pyplot as plt
import copy

WINDOW_SIZE = 30
NUM_FEATURES = 12  
INPUT_DIM = WINDOW_SIZE * NUM_FEATURES
def plot_training_results(history):
    epochs = range(1, len(history['train_loss']) + 1)
    
    plt.figure(figsize=(8, 5))

    plt.plot(epochs, history['train_loss'], 'r-o', label='Train Loss')
    plt.title('Training Loss over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('training_performance.png')
    plt.show()

def build_model():
    return NeuralNetwork([
        Dense(INPUT_DIM, 512),
        BatchNorm1D(512),
        ReLU(),
        Dropout(p=0.3),

        Dense(512, 256),
        BatchNorm1D(256),
        ReLU(),
        Dropout(p=0.25),

        Dense(256, 128),
        BatchNorm1D(128),
        ReLU(),
        Dropout(p=0.2),

        Dense(128, 64),
        BatchNorm1D(64),
        ReLU(),
        Dropout(p=0.15),

        Dense(64, 32),
        ReLU(),
        Dropout(p=0.1),

        Dense(32, 1),
        Sigmoid()
    ])

def find_best_threshold(val_preds, val_targets):
    thresholds = np.arange(0.3, 0.8, 0.01)
    best_acc = 0
    best_thresh = 0.5
    for thresh in thresholds:
        acc = np.mean((val_preds >= thresh).astype(int) == val_targets)
        if acc > best_acc:
            best_acc = acc
            best_thresh = thresh
    return best_thresh, best_acc

def accuracy(preds, targets, threshold=0.55):
    preds = (preds >= threshold).astype(int)
    targets = targets.astype(int)
    return np.mean(preds == targets)

def classification_metrics(preds, targets):
    preds = (preds >= 0.55).astype(int)
    targets = targets.astype(int)

    tp = np.sum((preds == 1) & (targets == 1))
    fp = np.sum((preds == 1) & (targets == 0))
    fn = np.sum((preds == 0) & (targets == 1))

    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)

    return precision, recall, f1

def train():
    print("🚀 Loading Dataset... Please wait, this might take a few minutes.")
    dataset = StockDataset('data/train.csv', window_size=WINDOW_SIZE)
    total_size = len(dataset)
    
    model = build_model()
    optimizer = Momentum(lr=0.002)  
    loss_fn = BinaryCrossEntropy()
    history = {
        'train_loss': []
    }

    print("🛠 Starting Training Process...")
    for epoch in range(25):  
        epoch_loss = 0
        batch_count = 0

        for i in range(0, total_size, 64):
            x_batch, y_batch = [], []
            for j in range(i, min(i + 64, total_size)):
                x, y = dataset.get_sample(j)
                x_batch.append(x)
                y_batch.append(y)

            x_batch = np.array(x_batch)
            y_batch = np.array(y_batch).reshape(-1, 1)

            preds = model.forward(x_batch, train=True)
            loss = loss_fn.forward(preds, y_batch)
            epoch_loss += loss
            batch_count += 1

            model.backward(loss_fn.backward())

            params_dict, grads_dict = {}, {}
            for l, layer in enumerate(model.layers):
                p = layer.params()
                g = layer.grads()
                if p:
                    for key in p:
                        uk = f"layer_{l}_{key}"
                        params_dict[uk] = p[key]
                        grads_dict[uk] = g[key]

            optimizer.update(params_dict, grads_dict)

        avg_loss = epoch_loss / batch_count
        history['train_loss'].append(avg_loss)

        print(f"✅ Epoch {epoch+1:02d} | Train Loss: {avg_loss:.6f}")

    plot_training_results(history)
    return model, dataset, 0.5  

def generate_final_submission(model, dataset, threshold=0.5):
    print("🎯 Generating predictions based on latest market data...")

    test_df = pd.read_csv('data/test.csv')
    train_full = pd.read_csv('data/train.csv').iloc[:10000]

    results = []
    unique_tickers = test_df['ID'].unique()

    train_full['Date'] = pd.to_datetime(train_full['Date'])
    train_full['Month'] = train_full['Date'].dt.month
    train_full['DayOfWeek'] = train_full['Date'].dt.dayofweek
    train_full['MA50'] = train_full.groupby('Ticker')['Close'].transform(lambda x: x.rolling(50).mean())
    train_full['MA200'] = train_full.groupby('Ticker')['Close'].transform(lambda x: x.rolling(200).mean())
    train_full['Daily_Return'] = train_full.groupby('Ticker')['Close'].transform(lambda x: x.pct_change())
    
    train_full['RSI'] = train_full.groupby('Ticker')['Close'].transform(lambda x: dataset.calculate_rsi(x))
    train_full['Volatility'] = train_full.groupby('Ticker')['Close'].transform(lambda x: x.rolling(20).std())
    train_full['Price_Momentum'] = train_full.groupby('Ticker')['Close'].transform(lambda x: x.pct_change(periods=5))
    train_full['Volume_MA'] = train_full.groupby('Ticker')['Volume'].transform(lambda x: x.rolling(20).mean())
    train_full['Volume_Ratio'] = train_full['Volume'] / train_full['Volume_MA']
    
    train_full = train_full.ffill().bfill().fillna(0)

    for ticker in unique_tickers:
        hist = train_full[train_full['Ticker'] == ticker]

        if len(hist) >= WINDOW_SIZE:
            x_matrix = hist[dataset.feature_cols].tail(WINDOW_SIZE).values
            x_matrix = (x_matrix - dataset.mean.values) / (dataset.std.values + 1e-8)
            x_input = x_matrix.flatten()
        else:
            x_input = np.zeros(INPUT_DIM)

        prediction = model.forward(x_input.reshape(1, -1), train=False)
        prob = prediction.item()
        label = 1 if prob >= threshold else 0  

        results.append({
           'ID': ticker,
           'Target': label
       })

    pd.DataFrame(results).to_csv('submission.csv', index=False)
    print(f"✨ submission.csv created successfully with threshold {threshold:.3f}!")

if __name__ == "__main__":
    trained_model, train_dataset, best_threshold = train()
    print("🎉 Training completed successfully!")

    generate_final_submission(trained_model, train_dataset, best_threshold)
    print("🏁 All tasks finished. Ready for Kaggle upload.")
