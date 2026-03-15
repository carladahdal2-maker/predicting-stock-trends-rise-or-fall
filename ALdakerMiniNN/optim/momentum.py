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
