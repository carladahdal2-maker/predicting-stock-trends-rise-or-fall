# 📁 PROJECT EXPORT FOR LLMs

## 📊 Project Information

- **Project Name**: `stock`
- **Generated On**: 2026-03-15 08:37:42 (America/Los_Angeles / GMT-07:00)
- **Total Files Processed**: 52
- **Export Tool**: Easy Whole Project to Single Text File for LLMs v1.1.0
- **Tool Author**: Jota / José Guilherme Pandolfi

### ⚙️ Export Configuration

| Setting | Value |
|---------|-------|
| Language | `en` |
| Max File Size | `1 MB` |
| Include Hidden Files | `false` |
| Output Format | `both` |

## 🌳 Project Structure

```
├── 📁 ALdakerMiniNN/
│   ├── 📁 __pycache__/
│   │   ├── 📄 __init__.cpython-312.pyc (689 B)
│   │   └── 📄 __init__.cpython-313.pyc (673 B)
│   ├── 📁 core/
│   │   ├── 📁 __pycache__/
│   │   │   ├── 📄 __init__.cpython-312.pyc (181 B)
│   │   │   ├── 📄 __init__.cpython-313.pyc (165 B)
│   │   │   ├── 📄 network.cpython-312.pyc (3.04 KB)
│   │   │   ├── 📄 network.cpython-313.pyc (3.09 KB)
│   │   │   ├── 📄 trainer.cpython-312.pyc (4.5 KB)
│   │   │   └── 📄 trainer.cpython-313.pyc (4.57 KB)
│   │   ├── 📄 __init__.py
│   │   ├── 📄 network.py (1.58 KB)
│   │   └── 📄 trainer.py (2.66 KB)
│   ├── 📁 layers/
│   │   ├── 📁 __pycache__/
│   │   │   ├── 📄 __init__.cpython-312.pyc (334 B)
│   │   │   ├── 📄 __init__.cpython-313.pyc (333 B)
│   │   │   ├── 📄 activations.cpython-312.pyc (3.29 KB)
│   │   │   ├── 📄 activations.cpython-313.pyc (3.42 KB)
│   │   │   ├── 📄 base.cpython-312.pyc (1.03 KB)
│   │   │   ├── 📄 base.cpython-313.pyc (1.07 KB)
│   │   │   ├── 📄 batchnorm.cpython-312.pyc (5.19 KB)
│   │   │   ├── 📄 batchnorm.cpython-313.pyc (5.21 KB)
│   │   │   ├── 📄 conv1d.cpython-312.pyc (3.63 KB)
│   │   │   ├── 📄 conv1d.cpython-313.pyc (3.64 KB)
│   │   │   ├── 📄 dense.cpython-312.pyc (3.7 KB)
│   │   │   ├── 📄 dense.cpython-313.pyc (3.81 KB)
│   │   │   ├── 📄 dropout.cpython-312.pyc (1.97 KB)
│   │   │   ├── 📄 dropout.cpython-313.pyc (2.01 KB)
│   │   │   ├── 📄 flatten.cpython-312.pyc (1.52 KB)
│   │   │   ├── 📄 flatten.cpython-313.pyc (1.56 KB)
│   │   │   ├── 📄 losses.cpython-312.pyc (5.8 KB)
│   │   │   └── 📄 losses.cpython-313.pyc (5.87 KB)
│   │   ├── 📄 __init__.py (124 B)
│   │   ├── 📄 activations.py (1.25 KB)
│   │   ├── 📄 base.py (367 B)
│   │   ├── 📄 batchnorm.py (3.02 KB)
│   │   ├── 📄 conv1d.py (1.91 KB)
│   │   ├── 📄 dense.py (1.99 KB)
│   │   ├── 📄 dropout.py (914 B)
│   │   ├── 📄 flatten.py (661 B)
│   │   └── 📄 losses.py (3.13 KB)
│   ├── 📁 optim/
│   │   ├── 📁 __pycache__/
│   │   │   ├── 📄 __init__.cpython-312.pyc (226 B)
│   │   │   ├── 📄 __init__.cpython-313.pyc (210 B)
│   │   │   ├── 📄 momentum.cpython-312.pyc (1.47 KB)
│   │   │   ├── 📄 momentum.cpython-313.pyc (1.48 KB)
│   │   │   ├── 📄 sgd.cpython-312.pyc (941 B)
│   │   │   └── 📄 sgd.cpython-313.pyc (985 B)
│   │   ├── 📄 __init__.py (32 B)
│   │   ├── 📄 momentum.py (744 B)
│   │   └── 📄 sgd.py (316 B)
│   └── 📄 __init__.py (388 B)
├── 📁 data/
│   ├── 📄 test.csv (111.23 KB)
│   └── 📄 train.csv (2.14 GB)
├── 📄 data_utils.py (3.26 KB)
└── 📄 main.py (6.62 KB)
```

## 📑 Table of Contents

**Project Files:**

- [📄 ALdakerMiniNN/core/__init__.py](#📄-aldakermininn-core-init-py)
- [📄 ALdakerMiniNN/core/network.py](#📄-aldakermininn-core-network-py)
- [📄 ALdakerMiniNN/core/trainer.py](#📄-aldakermininn-core-trainer-py)
- [📄 ALdakerMiniNN/layers/__init__.py](#📄-aldakermininn-layers-init-py)
- [📄 ALdakerMiniNN/layers/activations.py](#📄-aldakermininn-layers-activations-py)
- [📄 ALdakerMiniNN/layers/base.py](#📄-aldakermininn-layers-base-py)
- [📄 ALdakerMiniNN/layers/batchnorm.py](#📄-aldakermininn-layers-batchnorm-py)
- [📄 ALdakerMiniNN/layers/conv1d.py](#📄-aldakermininn-layers-conv1d-py)
- [📄 ALdakerMiniNN/layers/dense.py](#📄-aldakermininn-layers-dense-py)
- [📄 ALdakerMiniNN/layers/dropout.py](#📄-aldakermininn-layers-dropout-py)
- [📄 ALdakerMiniNN/layers/flatten.py](#📄-aldakermininn-layers-flatten-py)
- [📄 ALdakerMiniNN/layers/losses.py](#📄-aldakermininn-layers-losses-py)
- [📄 ALdakerMiniNN/optim/__init__.py](#📄-aldakermininn-optim-init-py)
- [📄 ALdakerMiniNN/optim/momentum.py](#📄-aldakermininn-optim-momentum-py)
- [📄 ALdakerMiniNN/optim/sgd.py](#📄-aldakermininn-optim-sgd-py)
- [📄 ALdakerMiniNN/__init__.py](#📄-aldakermininn-init-py)
- [📄 data_utils.py](#📄-data-utils-py)
- [📄 main.py](#📄-main-py)

---

## 📈 Project Statistics

| Metric | Count |
|--------|-------|
| Total Files | 52 |
| Total Directories | 9 |
| Text Files | 18 |
| Binary Files | 34 |
| Total Size | 2.14 GB |

### 📄 File Types Distribution

| Extension | Count |
|-----------|-------|
| `.pyc` | 32 |
| `.py` | 18 |
| `.csv` | 2 |

## 💻 File Code Contents

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `ALdakerMiniNN/__pycache__/__init__.cpython-312.pyc`
- `ALdakerMiniNN/__pycache__/__init__.cpython-313.pyc`

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `ALdakerMiniNN/core/__pycache__/__init__.cpython-312.pyc`
- `ALdakerMiniNN/core/__pycache__/__init__.cpython-313.pyc`
- `ALdakerMiniNN/core/__pycache__/network.cpython-312.pyc`
- `ALdakerMiniNN/core/__pycache__/network.cpython-313.pyc`
- `ALdakerMiniNN/core/__pycache__/trainer.cpython-312.pyc`
- `ALdakerMiniNN/core/__pycache__/trainer.cpython-313.pyc`

### <a id="📄-aldakermininn-core-init-py"></a>📄 `ALdakerMiniNN/core/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/core/__init__.py`
- **Relative Path**: `ALdakerMiniNN/core`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2025-12-25 13:01:18 (America/Los_Angeles / GMT-08:00)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-aldakermininn-core-network-py"></a>📄 `ALdakerMiniNN/core/network.py`

**File Info:**
- **Size**: 1.58 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/core/network.py`
- **Relative Path**: `ALdakerMiniNN/core`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-28 14:41:38 (America/Los_Angeles / GMT-08:00)
- **MD5**: `2be646c0430f1ecba60cec4b169344ab`
- **SHA256**: `52bb6307bda4e35ade757fb7395e52438eba5e0e92b07e6ee538e4765d038263`
- **Encoding**: ASCII

**File code content:**

```python
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

```

---

### <a id="📄-aldakermininn-core-trainer-py"></a>📄 `ALdakerMiniNN/core/trainer.py`

**File Info:**
- **Size**: 2.66 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/core/trainer.py`
- **Relative Path**: `ALdakerMiniNN/core`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-28 14:42:08 (America/Los_Angeles / GMT-08:00)
- **MD5**: `8ed17748ae908bf21415723f2408ff9c`
- **SHA256**: `7e9c4c8f74aa3ee3526989609ea68740f895a09289360843b85379060fa628ea`
- **Encoding**: ASCII

**File code content:**

```python
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

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `ALdakerMiniNN/layers/__pycache__/__init__.cpython-312.pyc`
- `ALdakerMiniNN/layers/__pycache__/__init__.cpython-313.pyc`
- `ALdakerMiniNN/layers/__pycache__/activations.cpython-312.pyc`
- `ALdakerMiniNN/layers/__pycache__/activations.cpython-313.pyc`
- `ALdakerMiniNN/layers/__pycache__/base.cpython-312.pyc`
- `ALdakerMiniNN/layers/__pycache__/base.cpython-313.pyc`
- `ALdakerMiniNN/layers/__pycache__/batchnorm.cpython-312.pyc`
- `ALdakerMiniNN/layers/__pycache__/batchnorm.cpython-313.pyc`
- `ALdakerMiniNN/layers/__pycache__/conv1d.cpython-312.pyc`
- `ALdakerMiniNN/layers/__pycache__/conv1d.cpython-313.pyc`
- `ALdakerMiniNN/layers/__pycache__/dense.cpython-312.pyc`
- `ALdakerMiniNN/layers/__pycache__/dense.cpython-313.pyc`
- `ALdakerMiniNN/layers/__pycache__/dropout.cpython-312.pyc`
- `ALdakerMiniNN/layers/__pycache__/dropout.cpython-313.pyc`
- `ALdakerMiniNN/layers/__pycache__/flatten.cpython-312.pyc`
- `ALdakerMiniNN/layers/__pycache__/flatten.cpython-313.pyc`
- `ALdakerMiniNN/layers/__pycache__/losses.cpython-312.pyc`
- `ALdakerMiniNN/layers/__pycache__/losses.cpython-313.pyc`

### <a id="📄-aldakermininn-layers-init-py"></a>📄 `ALdakerMiniNN/layers/__init__.py`

**File Info:**
- **Size**: 124 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/layers/__init__.py`
- **Relative Path**: `ALdakerMiniNN/layers`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-19 23:29:26 (America/Los_Angeles / GMT-08:00)
- **MD5**: `61adaa9ed7af89469a3f4006f447a2d5`
- **SHA256**: `a6df33d7778b919160f2dabcb5e9f236eab83cb563b22e5205765811ed36070a`
- **Encoding**: ASCII

**File code content:**

```python
from .flatten import Flatten
from .dropout import Dropout
from .batchnorm import BatchNorm1D
from .conv1d import Conv1D

```

---

### <a id="📄-aldakermininn-layers-activations-py"></a>📄 `ALdakerMiniNN/layers/activations.py`

**File Info:**
- **Size**: 1.25 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/layers/activations.py`
- **Relative Path**: `ALdakerMiniNN/layers`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-28 14:43:04 (America/Los_Angeles / GMT-08:00)
- **MD5**: `6d1480dd852fd4dabaf788dc1ba14b80`
- **SHA256**: `26c7a28ded00127ccb3d01b1e74c726cd9b92dea1c5c7105451cc2397f8cff89`
- **Encoding**: ASCII

**File code content:**

```python
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

```

---

### <a id="📄-aldakermininn-layers-base-py"></a>📄 `ALdakerMiniNN/layers/base.py`

**File Info:**
- **Size**: 367 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/layers/base.py`
- **Relative Path**: `ALdakerMiniNN/layers`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-28 14:43:26 (America/Los_Angeles / GMT-08:00)
- **MD5**: `dc1caf4a8471f490db5e293a4f36122a`
- **SHA256**: `db0a9596a6a785c3756cbf0437da0d1bf853cb0946a29a1ba56d574aaea23df0`
- **Encoding**: ASCII

**File code content:**

```python
class Layer:
   

    def forward(self, x, train: bool = True):
        raise NotImplementedError("forward() must be implemented by subclasses")

    def backward(self, dout):
        raise NotImplementedError("backward() must be implemented by subclasses")

    def params(self) -> dict:
        return {}

    def grads(self) -> dict:
        return {}
```

---

### <a id="📄-aldakermininn-layers-batchnorm-py"></a>📄 `ALdakerMiniNN/layers/batchnorm.py`

**File Info:**
- **Size**: 3.02 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/layers/batchnorm.py`
- **Relative Path**: `ALdakerMiniNN/layers`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-28 14:44:06 (America/Los_Angeles / GMT-08:00)
- **MD5**: `07e402ec1a0cafc5e84e409eea97968f`
- **SHA256**: `10600ea81687b95f64fc475f4aa9b920a78d5f1409fbd8f01499a5a42e5d26a2`
- **Encoding**: ASCII

**File code content:**

```python
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

```

---

### <a id="📄-aldakermininn-layers-conv1d-py"></a>📄 `ALdakerMiniNN/layers/conv1d.py`

**File Info:**
- **Size**: 1.91 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/layers/conv1d.py`
- **Relative Path**: `ALdakerMiniNN/layers`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-28 14:45:06 (America/Los_Angeles / GMT-08:00)
- **MD5**: `db13b3830bd328a088d7f7c6925f59c5`
- **SHA256**: `498d582b0f29b22ca19113cc50a71ce30d60fe79e544ddc102c842fb30b617e0`
- **Encoding**: ASCII

**File code content:**

```python
import numpy as np
from .base import Layer


class Conv1D(Layer):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride

        limit = np.sqrt(1.0 / (in_channels * kernel_size))
        self.W = np.random.uniform(
            -limit, limit,
            (out_channels, in_channels, kernel_size)
        )
        self.b = np.zeros((out_channels,))

        self.x = None
        self.dW = np.zeros_like(self.W)
        self.db = np.zeros_like(self.b)

    def forward(self, x, train=True):
        x = np.asarray(x)
        self.x = x

        N, C, L = x.shape
        out_len = (L - self.kernel_size) // self.stride + 1
        out = np.zeros((N, self.out_channels, out_len))

        for n in range(N):
            for oc in range(self.out_channels):
                for i in range(out_len):
                    start = i * self.stride
                    end = start + self.kernel_size
                    out[n, oc, i] = np.sum(
                        x[n, :, start:end] * self.W[oc]
                    ) + self.b[oc]

        return out

    def backward(self, dout):
        N, C, L = self.x.shape
        _, OC, out_len = dout.shape

        dx = np.zeros_like(self.x)

        for n in range(N):
            for oc in range(OC):
                for i in range(out_len):
                    start = i * self.stride
                    end = start + self.kernel_size

                    self.dW[oc] += dout[n, oc, i] * self.x[n, :, start:end]
                    dx[n, :, start:end] += dout[n, oc, i] * self.W[oc]
                    self.db[oc] += dout[n, oc, i]

        return dx

    def params(self):
        return {"W": self.W, "b": self.b}

    def grads(self):
        return {"W": self.dW, "b": self.db}

```

---

### <a id="📄-aldakermininn-layers-dense-py"></a>📄 `ALdakerMiniNN/layers/dense.py`

**File Info:**
- **Size**: 1.99 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/layers/dense.py`
- **Relative Path**: `ALdakerMiniNN/layers`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-28 14:46:28 (America/Los_Angeles / GMT-08:00)
- **MD5**: `474ceebcd469250004332dc98d87409f`
- **SHA256**: `e02f3ecb22d7395877b9185a2c60faaff68c2e9d691ecc22fcfb438399e103d3`
- **Encoding**: ASCII

**File code content:**

```python
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

```

---

### <a id="📄-aldakermininn-layers-dropout-py"></a>📄 `ALdakerMiniNN/layers/dropout.py`

**File Info:**
- **Size**: 914 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/layers/dropout.py`
- **Relative Path**: `ALdakerMiniNN/layers`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-28 14:49:00 (America/Los_Angeles / GMT-08:00)
- **MD5**: `38dbc8c4c9a49c4542c94fa191849601`
- **SHA256**: `97abba836293a12d87e4ffb31772e6773f1a7c48ddaed4fc31b22f180b91fe87`
- **Encoding**: ASCII

**File code content:**

```python
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
```

---

### <a id="📄-aldakermininn-layers-flatten-py"></a>📄 `ALdakerMiniNN/layers/flatten.py`

**File Info:**
- **Size**: 661 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/layers/flatten.py`
- **Relative Path**: `ALdakerMiniNN/layers`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-28 14:49:12 (America/Los_Angeles / GMT-08:00)
- **MD5**: `04627b026676c7786b5547334d3244e1`
- **SHA256**: `87651eeaac9a8e94a8633b3e785d4d318d5f4238c7faea5b948f6a2901fc7782`
- **Encoding**: ASCII

**File code content:**

```python
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
```

---

### <a id="📄-aldakermininn-layers-losses-py"></a>📄 `ALdakerMiniNN/layers/losses.py`

**File Info:**
- **Size**: 3.13 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/layers/losses.py`
- **Relative Path**: `ALdakerMiniNN/layers`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-28 14:49:50 (America/Los_Angeles / GMT-08:00)
- **MD5**: `099e00cf4c0753eb8b259d59f93302a7`
- **SHA256**: `d41140baf80399ec3001c6c40d75e7c4f50917b2fc48704d48175729e774cfde`
- **Encoding**: ASCII

**File code content:**

```python
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
```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `ALdakerMiniNN/optim/__pycache__/__init__.cpython-312.pyc`
- `ALdakerMiniNN/optim/__pycache__/__init__.cpython-313.pyc`
- `ALdakerMiniNN/optim/__pycache__/momentum.cpython-312.pyc`
- `ALdakerMiniNN/optim/__pycache__/momentum.cpython-313.pyc`
- `ALdakerMiniNN/optim/__pycache__/sgd.cpython-312.pyc`
- `ALdakerMiniNN/optim/__pycache__/sgd.cpython-313.pyc`

### <a id="📄-aldakermininn-optim-init-py"></a>📄 `ALdakerMiniNN/optim/__init__.py`

**File Info:**
- **Size**: 32 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/optim/__init__.py`
- **Relative Path**: `ALdakerMiniNN/optim`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2025-12-26 18:13:00 (America/Los_Angeles / GMT-08:00)
- **MD5**: `08f998536d6d869f30fc11123df97b05`
- **SHA256**: `3b33b558389535f7676792310bf4042f12bd7bbd7d958cd359f37c69f54251bc`
- **Encoding**: ASCII

**File code content:**

```python
from .momentum import Momentum

```

---

### <a id="📄-aldakermininn-optim-momentum-py"></a>📄 `ALdakerMiniNN/optim/momentum.py`

**File Info:**
- **Size**: 744 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/optim/momentum.py`
- **Relative Path**: `ALdakerMiniNN/optim`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2025-12-30 13:23:50 (America/Los_Angeles / GMT-08:00)
- **MD5**: `b4ab514273f5c83a1f96ad4d806b1394`
- **SHA256**: `ad0e4a7cedac57077b974887b6c0abcb08f9830d0958cf0656ae8652dc3be639`
- **Encoding**: ASCII

**File code content:**

```python
class Momentum:
   

    def __init__(self, lr: float = 0.01, momentum: float = 0.9):
        if lr <= 0:
            raise ValueError("Learning rate must be positive.")
        if not (0.0 <= momentum < 1.0):
            raise ValueError("Momentum must be in [0, 1).")

        self.lr = lr
        self.momentum = momentum
        self.velocity = {}  

    def update(self, params: dict, grads: dict):
        for key in params.keys():
            if key not in self.velocity:
                self.velocity[key] = grads[key] * 0.0

            self.velocity[key] = (
                self.momentum * self.velocity[key]
                - self.lr * grads[key]
            )

            params[key] += self.velocity[key]

```

---

### <a id="📄-aldakermininn-optim-sgd-py"></a>📄 `ALdakerMiniNN/optim/sgd.py`

**File Info:**
- **Size**: 316 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/optim/sgd.py`
- **Relative Path**: `ALdakerMiniNN/optim`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2025-12-30 13:23:50 (America/Los_Angeles / GMT-08:00)
- **MD5**: `a6c9500a978c1a82f1c9c31fafc50637`
- **SHA256**: `0f9252bc401efd8dccccd08cc868cb5557acab986a747d48e1ea03cd5c025f26`
- **Encoding**: ASCII

**File code content:**

```python
class SGD:
    

    def __init__(self, lr: float = 0.01):
        if lr <= 0:
            raise ValueError("Learning rate must be positive.")
        self.lr = lr

    def update(self, params: dict, grads: dict):
       
        for key in params.keys():
            params[key] -= self.lr * grads[key]

```

---

### <a id="📄-aldakermininn-init-py"></a>📄 `ALdakerMiniNN/__init__.py`

**File Info:**
- **Size**: 388 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `ALdakerMiniNN/__init__.py`
- **Relative Path**: `ALdakerMiniNN`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2025-12-30 20:35:10 (America/Los_Angeles / GMT-08:00)
- **MD5**: `5df9a7d33c4d0a6ab2ff299b4e86eb32`
- **SHA256**: `adaa0128dfedef933bfe3210f71825bc2283242c5627d7f6f8b27c80bcc9e0db`
- **Encoding**: ASCII

**File code content:**

```python

from .core.network import NeuralNetwork
from .core.trainer import Trainer

from .layers.dense import Dense
from .layers.flatten import Flatten
from .layers.activations import ReLU, Sigmoid, Tanh, Linear
from .layers.losses import SoftmaxCrossEntropy, MeanSquaredError

from .optim.sgd import SGD
from .optim.momentum import Momentum
from .layers.batchnorm import BatchNorm1D

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `data/test.csv`
- `data/train.csv`

### <a id="📄-data-utils-py"></a>📄 `data_utils.py`

**File Info:**
- **Size**: 3.26 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `data_utils.py`
- **Relative Path**: `root`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-30 04:00:14 (America/Los_Angeles / GMT-08:00)
- **MD5**: `e8da5e52cd845faf21dab3a733267529`
- **SHA256**: `30dab101a28d445b03d8c7feb13d5d6c03bf9d58d2c992ee173bf10294ba5eaa`
- **Encoding**: ASCII

**File code content:**

```python
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
```

---

### <a id="📄-main-py"></a>📄 `main.py`

**File Info:**
- **Size**: 6.62 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `main.py`
- **Relative Path**: `root`
- **Created**: 2026-01-29 05:38:36 (America/Los_Angeles / GMT-08:00)
- **Modified**: 2026-01-30 04:00:09 (America/Los_Angeles / GMT-08:00)
- **MD5**: `8054242293b1aaebdf5bc4489ec57c94`
- **SHA256**: `5d90996e7cc0ce95300223a1c84ac4794061137d8eb4c742f94484c93811ba4c`
- **Encoding**: ASCII

**File code content:**

```python
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

```

---

