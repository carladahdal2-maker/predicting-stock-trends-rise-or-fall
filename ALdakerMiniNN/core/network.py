from __future__ import annotations
from typing import List, Dict, Any, Iterable, Tuple

import numpy as np
from ALdakerMiniNN.layers.base import Layer


class NeuralNetwork:
    

    def __init__(self, layers: List[Layer]):
        if not isinstance(layers, list) or len(layers) == 0:
            raise ValueError("NeuralNetwork expects a non-empty list of layers.")
        self.layers = layers

    def forward(self, x, train: bool = True):
        out = x
        for layer in self.layers:
            out = layer.forward(out, train=train)
        return out

    def predict(self, x):
        return self.forward(x, train=False)

    def backward(self, dout):
        grad = dout
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
        return grad

    def params(self) -> Dict[str, Any]:
       
        out: Dict[str, Any] = {}
        for i, layer in enumerate(self.layers):
            p = layer.params()
            for name, value in p.items():
                out[f"{i}/{name}"] = value
        return out

    def grads(self) -> Dict[str, Any]:
       
        out: Dict[str, Any] = {}
        for i, layer in enumerate(self.layers):
            g = layer.grads()
            for name, value in g.items():
                out[f"{i}/{name}"] = value
        return out

    def params_and_grads(self) -> Iterable[Tuple[np.ndarray, np.ndarray]]:
       
        for layer in self.layers:
            p = layer.params()
            g = layer.grads()
            for k in p.keys():
                yield p[k], g[k]
