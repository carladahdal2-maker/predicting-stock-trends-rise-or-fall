import numpy as np
from .base import Layer


class Flatten(Layer):
  

    def __init__(self):
        self._orig_shape = None

    def forward(self, x, train: bool = True):
        x = np.asarray(x)
        self._orig_shape = x.shape

        if x.ndim < 2:
            raise ValueError(f"Flatten expects at least 2D input (N, ...). Got shape {x.shape}")

        N = x.shape[0]
        return x.reshape(N, -1)

    def backward(self, dout):
        if self._orig_shape is None:
            raise RuntimeError("Flatten.backward() called before forward().")

        dout = np.asarray(dout)
        return dout.reshape(self._orig_shape)