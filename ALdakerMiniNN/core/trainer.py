import numpy as np


class Trainer:
    def __init__(self, model, loss_fn, optimizer, seed: int = 42):
        self.model = model
        self.loss_fn = loss_fn
        self.optimizer = optimizer
        self.rng = np.random.default_rng(seed)

    def _iter_minibatches(self, X, y, batch_size: int, shuffle: bool = True):
        N = X.shape[0]
        idx = np.arange(N)
        if shuffle:
            self.rng.shuffle(idx)

        for start in range(0, N, batch_size):
            batch_idx = idx[start:start + batch_size]
            yield X[batch_idx], y[batch_idx]

    def accuracy(self, X, y):
        scores = self.model.predict(X)  
        if scores.ndim == 1 or (scores.ndim == 2 and scores.shape[1] == 1):
            preds = (scores.reshape(-1) >= 0.5).astype(int)
        else:
            preds = np.argmax(scores, axis=1)

        y_arr = np.asarray(y)
        if y_arr.ndim == 2:
            y_arr = np.argmax(y_arr, axis=1)

        return float(np.mean(preds == y_arr))

    def train_step(self, Xb, yb):
        
        scores = self.model.forward(Xb, train=True)
        loss = self.loss_fn.forward(scores, yb)
        
        dscores = self.loss_fn.backward()
        self.model.backward(dscores)

        
        self.optimizer.update(self.model.params(), self.model.grads())

        return float(loss)

    def fit(self, X_train, y_train, X_test=None, y_test=None, epochs: int = 20, batch_size: int = 32, verbose: bool = True):
        X_train = np.asarray(X_train)
        y_train = np.asarray(y_train)

        history = {
            "loss": [],
            "train_acc": [],
            "test_acc": []
        }

        for ep in range(1, epochs + 1):
            losses = []
            for Xb, yb in self._iter_minibatches(X_train, y_train, batch_size=batch_size, shuffle=True):
                losses.append(self.train_step(Xb, yb))

            avg_loss = float(np.mean(losses)) if losses else float("nan")
            history["loss"].append(avg_loss)

            train_acc = self.accuracy(X_train, y_train)
            history["train_acc"].append(train_acc)

            test_acc = None
            if X_test is not None and y_test is not None:
                test_acc = self.accuracy(np.asarray(X_test), np.asarray(y_test))
                history["test_acc"].append(test_acc)

            if verbose:
                if test_acc is None:
                    print(f"Epoch {ep:03d} | loss={avg_loss:.6f} | train_acc={train_acc:.4f}")
                else:
                    print(f"Epoch {ep:03d} | loss={avg_loss:.6f} | train_acc={train_acc:.4f} | test_acc={test_acc:.4f}")

        return history
