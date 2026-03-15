import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class StockDataset:
    def __init__(self, csv_file, window_size=30):
        self.df = pd.read_csv(csv_file)
        if 'train' in csv_file:
            self.df = self.df.iloc[:500000]
        self.window_size = window_size
        
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        
        self.df = self.df.sort_values(['Ticker', 'Date']) 
        
        self.df['MA50'] = self.df['Close'].rolling(window=50).mean()
        self.df['MA200'] = self.df['Close'].rolling(window=200).mean()
        self.df['Daily_Return'] = self.df['Close'].pct_change()
        
        self.df['RSI'] = self.calculate_rsi(self.df['Close'])
        self.df['Volatility'] = self.df['Close'].rolling(window=20).std()
        self.df['Price_Momentum'] = self.df['Close'].pct_change(periods=5)
        self.df['Volume_MA'] = self.df['Volume'].rolling(window=20).mean()
        self.df['Volume_Ratio'] = self.df['Volume'] / self.df['Volume_MA']
        
        self.feature_cols = ['Open', 'High', 'Low', 'Close', 'Volume', 'MA50', 'MA200', 
                           'Daily_Return', 'RSI', 'Volatility', 'Price_Momentum', 'Volume_Ratio']
        
        self.df['Target'] = (self.df['Close'].shift(-30) > self.df['Close']).astype(int)
        
        self.data = self.df.dropna().reset_index(drop=True)
        
        self.mean = self.data[self.feature_cols].mean()
        self.std = self.data[self.feature_cols].std()
        self.data[self.feature_cols] = (self.data[self.feature_cols] - self.mean) / (self.std + 1e-8)

    def calculate_rsi(self, prices, period=14):
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def __len__(self):
        return len(self.data) - self.window_size

    def get_sample(self, idx):
        window = self.data.iloc[idx : idx + self.window_size][self.feature_cols].values
        target = self.data.iloc[idx + self.window_size - 1]['Target']
        return window.flatten(), target
    
class DataLoader:
    def __init__(self, dataset, batch_size=32, shuffle=True):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.indices = np.arange(len(self.dataset))

    def __iter__(self):
        if self.shuffle:
            np.random.shuffle(self.indices)
        for start in range(0, len(self.indices), self.batch_size):
            batch_indices = self.indices[start : start + self.batch_size]
            x_batch, y_batch = [], []
            for idx in batch_indices:
                x, y = self.dataset.get_sample(idx)
                x_batch.append(x)
                y_batch.append(y)
            yield np.array(x_batch), np.array(y_batch)

    def __len__(self):
        return int(np.ceil(len(self.dataset) / self.batch_size))

def plot_stock_sample(df, n_days=500):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'].iloc[:n_days], df['Close'].iloc[:n_days], label='Close Price')
    plt.title("Stock Price Sample")
    plt.legend()
    plt.show()
    plt.close()