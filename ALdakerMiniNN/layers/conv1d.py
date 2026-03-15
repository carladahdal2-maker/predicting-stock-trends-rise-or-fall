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
