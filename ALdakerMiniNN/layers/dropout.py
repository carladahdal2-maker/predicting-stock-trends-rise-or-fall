import numpy as np
from .base import Layer


class Dropout(Layer):
    

    def __init__(self, p: float = 0.5, seed: int | None = None):
        if not (0.0 <= p < 1.0):
            raise ValueError("Dropout p must be in [0, 1).")
        self.p = float(p)
        self.keep_prob = 1.0 - self.p
        self._mask = None
        self._rng = np.random.default_rng(seed)

    def forward(self, x, train: bool = True):
        x = np.asarray(x)

        if (not train) or self.p == 0.0:
            self._mask = None
            return x

        self._mask = (self._rng.random(size=x.shape) < self.keep_prob)

        out = (x * self._mask) / self.keep_prob
        return out

    def backward(self, dout):
        dout = np.asarray(dout)

        if self._mask is None or self.p == 0.0:
            return dout

        dx = (dout * self._mask) / self.keep_prob
        return dx