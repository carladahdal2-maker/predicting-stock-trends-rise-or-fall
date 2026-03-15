import numpy as np


class SoftmaxCrossEntropy:
  

    def __init__(self):
        self.probs = None
        self.y = None
        self.N = None

    def forward(self, scores, y):
       
        scores = np.asarray(scores, dtype=float)
        y = np.asarray(y)

        if scores.ndim != 2:
            raise ValueError(f"SoftmaxCrossEntropy expects scores 2D (N, C). Got {scores.shape}")

        N, C = scores.shape
        self.N = N
        self.y = y

        
        shifted = scores - np.max(scores, axis=1, keepdims=True)
        exp_scores = np.exp(shifted)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        self.probs = probs

      
        if y.ndim == 1:
            if y.shape[0] != N:
                raise ValueError("y shape mismatch with batch size.")
            correct_logprobs = -np.log(probs[np.arange(N), y] + 1e-12)
            loss = np.mean(correct_logprobs)
        elif y.ndim == 2:
            if y.shape != (N, C):
                raise ValueError("one-hot y shape must be (N, C)")
            correct_logprobs = -np.sum(y * np.log(probs + 1e-12), axis=1)
            loss = np.mean(correct_logprobs)
        else:
            raise ValueError("y must be 1D (labels) or 2D (one-hot).")

        return loss

    def backward(self):
       
        if self.probs is None or self.y is None or self.N is None:
            raise RuntimeError("backward() called before forward().")

        ds = self.probs.copy()

        if self.y.ndim == 1:
            ds[np.arange(self.N), self.y] -= 1.0
            ds /= self.N
        else:
            # one-hot
            ds = (ds - self.y) / self.N

        return ds


class MeanSquaredError:
  

    def __init__(self):
        self.pred = None
        self.target = None
        self.N = None

    def forward(self, pred, target):
        pred = np.asarray(pred, dtype=float)
        target = np.asarray(target, dtype=float)

        if pred.shape != target.shape:
            raise ValueError(f"pred and target must have same shape. Got {pred.shape} vs {target.shape}")

        self.pred = pred
        self.target = target
        self.N = pred.shape[0]

        loss = np.mean((pred - target) ** 2)
        return loss

    def backward(self):
        if self.pred is None or self.target is None or self.N is None:
            raise RuntimeError("backward() called before forward().")
        return (2.0 / self.N) * (self.pred - self.target)

class BinaryCrossEntropy:
    def __init__(self):
        self.pred = None
        self.target = None
        self.eps = 1e-12

    def forward(self, pred, target):
        pred = np.asarray(pred, dtype=float)
        target = np.asarray(target, dtype=float)

        pred = np.clip(pred, self.eps, 1.0 - self.eps)

        self.pred = pred
        self.target = target

        loss = -np.mean(
            target * np.log(pred) + (1 - target) * np.log(1 - pred)
        )
        return loss

    def backward(self):
        pred = self.pred
        target = self.target
        return (pred - target) / (pred * (1 - pred) + self.eps)