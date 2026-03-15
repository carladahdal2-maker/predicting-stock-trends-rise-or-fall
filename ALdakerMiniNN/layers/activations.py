import numpy as np
from .base import Layer


class Linear(Layer):

    def forward(self, x, train: bool = True):
        self._x_shape = np.asarray(x).shape
        return x

    def backward(self, dout):
        return dout


class ReLU(Layer):

    def __init__(self):
        self._mask = None

    def forward(self, x, train: bool = True):
        x = np.asarray(x)
        self._mask = (x > 0)
        return np.maximum(0, x)

    def backward(self, dout):
        dout = np.asarray(dout)
        return dout * self._mask


class Sigmoid(Layer):

    def __init__(self):
        self._out = None

    def forward(self, x, train: bool = True):
        x = np.asarray(x)
        x = np.clip(x, -50, 50)
        out = 1.0 / (1.0 + np.exp(-x))
        self._out = out
        return out

    def backward(self, dout):
        dout = np.asarray(dout)
        return dout * (self._out * (1.0 - self._out))


class Tanh(Layer):

    def __init__(self):
        self._out = None

    def forward(self, x, train: bool = True):
        x = np.asarray(x)
        out = np.tanh(x)
        self._out = out
        return out

    def backward(self, dout):
        dout = np.asarray(dout)
        return dout * (1.0 - self._out ** 2)
