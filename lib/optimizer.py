import vector as np

class SGD:

  """ Stochastic gradient Descent """

  def __init__(self, lr=0.01):
    self.lr = lr

  def update(self, params, grads):
    for key in params.keys():
      params[key] = params[key] - (grads[key] * self.lr)

class Momentum:

  """ Momentum SGD """

  def __init__(self, lr=0.01, momentum=0.9):
    self.lr = lr
    self.momentum = momentum
    self.v = None

  def update(self, params, grads):
    if self.v is None:
      self.v = {}
      for key, val in params.items():
        dmen = val.get_demension()
        self.v[key] = np.arange([0 for _ in range(reduce(lambda x, y : x*y, dmen))]).reshape(dmen)
    
    for key in params.keys():
      self.v[key] = (self.v[key]*self.momentum) + (grads[key]*self.lr)
      params[key] = params[key] - self.v[key] 

class Nesterov:

  """ Nesterov's Accelerated Gradient (http://arxiv.org/abs/1212.0901)"""

  def __init__(self, lr=0.01, momentum=0.9):
    self.lr = lr
    self.momentum = momentum
    self.v = None

  def update(self, params, grads):
    if self.v is None:
      self.v = {}
      for key, val in params.items():
        self.v[key] = np.arange([0 for _ in range(reduce(lambda x, y : x*y, dmen))]).reshape(dmen)
    
    for key in params.keys():
      # v(t) = momentum * v(t-1) - learning_rate * dL/dw
      # w(t) = w(t-1) + momentum * v(t+1) - learning_rate * dL/dw
      self.v[key] = (self.v[key]*self.momentum) - grads[key]*self.lr
      params[key] = params[key] + self.v[key]*self.momentum*self.momentum - grads[key]*(1+self.momentum)*self.lr


