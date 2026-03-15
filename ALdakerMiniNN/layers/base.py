class Layer:
   

    def forward(self, x, train: bool = True):
        raise NotImplementedError("forward() must be implemented by subclasses")

    def backward(self, dout):
        raise NotImplementedError("backward() must be implemented by subclasses")

    def params(self) -> dict:
        return {}

    def grads(self) -> dict:
        return {}