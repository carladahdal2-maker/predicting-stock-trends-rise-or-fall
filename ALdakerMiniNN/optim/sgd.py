class SGD:
    

    def __init__(self, lr: float = 0.01):
        if lr <= 0:
            raise ValueError("Learning rate must be positive.")
        self.lr = lr

    def update(self, params: dict, grads: dict):
       
        for key in params.keys():
            params[key] -= self.lr * grads[key]
