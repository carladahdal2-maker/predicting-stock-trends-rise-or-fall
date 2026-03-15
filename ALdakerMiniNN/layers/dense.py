import numpy as np
from .base import Layer


class Dense(Layer):
  

    def __init__(self, in_features: int, out_features: int, weight_scale: float = None, auto_flatten: bool = False):
        self.in_features = int(in_features)
        self.out_features = int(out_features)
        self.auto_flatten = bool(auto_flatten)

        if weight_scale is None:
            weight_scale = np.sqrt(1.0 / self.in_features)

        self.W = np.random.randn(self.in_features, self.out_features) * weight_scale
        self.b = np.zeros((1, self.out_features), dtype=float)

        self._x2d = None
        self._x_orig_shape = None

        self.dW = np.zeros_like(self.W)
        self.db = np.zeros_like(self.b)

    def forward(self, x, train: bool = True):
        x = np.asarray(x)
        self._x_orig_shape = x.shape

        if x.ndim != 2:
            if not self.auto_flatten:
                raise ValueError(f"Dense expects 2D input (N, D). Got shape {x.shape}. "
                                 f"Flatten first or set auto_flatten=True.")
            x = x.reshape(x.shape[0], -1)

        if x.shape[1] != self.in_features:
            raise ValueError(f"Dense expected in_features={self.in_features}, but got x.shape[1]={x.shape[1]}")

        self._x2d = x  
        out = x @ self.W + self.b  
        return out

    def backward(self, dout):
        dout = np.asarray(dout)
        x = self._x2d
        if x is None:
            raise RuntimeError("Dense.backward() called before forward().")

       

        self.dW = x.T @ dout                            
        self.db = np.sum(dout, axis=0, keepdims=True)   
        dx = dout @ self.W.T                            

       
        if self.auto_flatten and len(self._x_orig_shape) != 2:
            dx = dx.reshape(self._x_orig_shape)

        return dx

    def params(self) -> dict:
        return {"W": self.W, "b": self.b}

    def grads(self) -> dict:
        return {"W": self.dW, "b": self.db}
