import numpy as np
from .base import Layer


class BatchNorm1D(Layer):
 

    def __init__(self, num_features: int, momentum: float = 0.9, eps: float = 1e-5):
        if num_features <= 0:
            raise ValueError("num_features must be positive.")
        if not (0.0 < momentum < 1.0):
            raise ValueError("momentum must be in (0, 1).")
        if eps <= 0:
            raise ValueError("eps must be positive.")

        self.D = int(num_features)
        self.momentum = float(momentum)
        self.eps = float(eps)

        self.gamma = np.ones((self.D,), dtype=float)
        self.beta = np.zeros((self.D,), dtype=float)

        self.running_mean = np.zeros((self.D,), dtype=float)
        self.running_var = np.ones((self.D,), dtype=float)

        self._x = None
        self._xhat = None
        self._mu = None
        self._var = None
        self._inv_std = None

        self.dgamma = np.zeros_like(self.gamma)
        self.dbeta = np.zeros_like(self.beta)

    def forward(self, x, train: bool = True):
        x = np.asarray(x)
        if x.ndim != 2:
            raise ValueError(f"BatchNorm1D expects 2D input (N, D). Got shape {x.shape}")
        if x.shape[1] != self.D:
            raise ValueError(f"BatchNorm1D expected D={self.D}, got {x.shape[1]}")

        if train:
            mu = x.mean(axis=0)
            var = x.var(axis=0)
            inv_std = 1.0 / np.sqrt(var + self.eps)
            xhat = (x - mu) * inv_std
            out = self.gamma * xhat + self.beta

            self.running_mean = self.momentum * self.running_mean + (1 - self.momentum) * mu
            self.running_var = self.momentum * self.running_var + (1 - self.momentum) * var

            self._x = x
            self._xhat = xhat
            self._mu = mu
            self._var = var
            self._inv_std = inv_std
            return out

        
        inv_std = 1.0 / np.sqrt(self.running_var + self.eps)
        xhat = (x - self.running_mean) * inv_std
        out = self.gamma * xhat + self.beta

        self._x = None
        self._xhat = None
        self._mu = None
        self._var = None
        self._inv_std = None
        return out

    def backward(self, dout):
        dout = np.asarray(dout)
        if dout.ndim != 2:
            raise ValueError(f"BatchNorm1D backward expects 2D dout. Got {dout.shape}")

        if self._x is None:
            return dout

        x = self._x
        xhat = self._xhat
        inv_std = self._inv_std
        N = x.shape[0]

        self.dbeta = dout.sum(axis=0)
        self.dgamma = np.sum(dout * xhat, axis=0)

        dxhat = dout * self.gamma  # (N, D)

        sum_dxhat = dxhat.sum(axis=0)
        sum_dxhat_xhat = np.sum(dxhat * xhat, axis=0)
        dx = (1.0 / N) * inv_std * (N * dxhat - sum_dxhat - xhat * sum_dxhat_xhat)

        return dx

    def params(self):
        return {"gamma": self.gamma, "beta": self.beta}

    def grads(self):
        return {"gamma": self.dgamma, "beta": self.dbeta}
