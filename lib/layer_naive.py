import vector as ve
import perceptron as pe
import layer as la
import loss as lo
import usr_math as um

e = um.natual()

class MulLayer:
  def __init__(self):
    self.x = None
    self.y = None

  def forward(self, x, y):
    self.x = x
    self.y = y
    out = x * y

    return out

  def backward(self, dout):
    dx = dout * self.y
    dy = dout * self.x

    return dx, dy

class AddLayer:
  def __init__(self):
    pass

  def forward(self, x, y):
    out = x + y
    return out

  def backward(self, dout):
    dx = dout * 1
    dy = dout * 1

    return dx, dy

class Relu:
  def __init__(self):
    self.mask = None

  def forward(self, x):
    if (type(x) == type(1)) or (type(x) == type(1.0)) :
      if x >= 0:
        out = x
      else :
        out = 0
    elif (type(x) == type(ve.arange([1]))) :
      #print "**********"
      dmen = x.get_demension()
      x.reshape(1, reduce(lambda x,y : x*y, dmen))
      x_lst = x.get_origin_list()
      out = ve.arange(list(map(lambda x: x if x >= 0 else 0, x_lst))).reshape(dmen)

    return out

  def backward(self, dout):
    if (type(dout) == type(1)) or (type(dout) == type(1.0)) :
      if x >= 0:
        dx = dout
      else :
        dx = 0
    elif (type(dout) == type(ve.arange([1]))) :
      dmen = dout.get_demension()
      dout.reshape(1, reduce(lambda x,y : x*y, dmen))
      dout_lst = dout.get_origin_list()
      dx = ve.arange(list(map(lambda x: x if x >= 0 else 0, dout_lst))).reshape(dmen)

    return dx

class Sigmoid:
  def __init__(self):
    self.out = None

  def forward(self, x):
    if (type(x) == type(1)) or (type(x) == type(1.0)) :
     out = 1 / (1 + e._e**(x*(-1)))
    elif (type(x) == type(ve.arange([1]))) :
      print "%% Sigmoid forward %%"
      print x
      dmen = x.get_demension()
      x.reshape(1, reduce(lambda x,y : x*y, dmen))
      x_lst = x.get_origin_list()
      out = ve.arange(list(map(lambda x: (1 / (1 + e._e**(x*(-1)))), x_lst))).reshape(dmen)
      print out

    self.out = out
    return out

  def backward(self, dout):
    if (type(dout) == type(1)) or (type(dout) == type(1.0)) :
      dx = dout * (1.0 - self.out) * self.out
    elif (type(dout) == type(ve.arange([1]))) :
      print "%% Sigmoid backward %%"
      print dout
      print self.out
      dout_dmen = dout.get_demension()
      out_dmen = self.out.get_demension()
      dout.reshape(1, reduce(lambda x,y : x*y, dout_dmen))
      self.out.reshape(1, reduce(lambda x,y : x*y, out_dmen))

      dout_lst = dout.get_origin_list()
      out_lst = self.out.get_origin_list()

      dx = ve.arange(list(map(lambda x,y: (x*(1.0-y)*y), dout_lst, out_lst))).reshape(dout_dmen)
      self.out.reshape(out_dmen)

    print dx

    return dx

class MatMul:
  def __init__(self, W):
    self.params = W
    self.grads = ve.zeros_like(W)
    self.x = None

  def forward(self, x):
    W = self.params
    out = x * W
    self.x = x
    return out

  def backward(self, dout):
    W = self.params
    dx = dout * W.transpose()
    dW = self.x.transpose() * dout
    self.grads = dW
    return dx

class Affine:
  def __init__(self, W, b):
    self.W = W
    self.b = b
    self.x = None
    self.dW = None
    self.db = None

  def forward(self, x):
    self.x = x
    out = self.x * self.W + self.b
    print "%% lib/layer_naive.py forward %%"
    print "******************************"
    print self.x
    print self.W
    print self.b
    print out
    print "******************************"
    
    return out
  
  def backward(self, dout):
    print "%% lib/layer_naive.py backward %%"
    print "******************************"
    print dout
    print self.x
    print self.W
    print self.b

    dx = dout * self.W.transpose()

    self.dW = self.x.transpose() * dout
    self.db = dout

    print self.dW
    print self.db
    print "*******************************"

    return dx

class SoftmaxWithLoss:
  def __init__(self):
    self.loss = None
    self.y = None
    self.t = None

  def forward(self, x, t):
    print "<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>"
    print x
    self.t = t
    self.y = la.softmax(x)
    self.loss = lo.cross_entropy_error(self.y, self.t)

    print self.t
    print self.y
    print self.loss
    print "<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>"

    return self.loss

  def backward(self, dout=1):
    batch_size = self.t.get_demension()[1]
    #TODO
    print "*********xxx**********************"
    print self.y
    print self.t

    #dx = (self.y - self.t) * (1.0/batch_size)
    dmen = self.y.get_demension()
    self.y.reshape(1, reduce(lambda x, y : x*y, dmen))
    
    dx_lst = self.y.get_origin_list()
    dx = ve.arange(dx_lst).reshape(dmen) 
    self.y.reshape(dmen)
    
    dx = (dx - self.t)

    print "**********yyy**********************"
    print self.y
    print self.t
    print self.loss
    print dx
    print "**********zzz*********************"

    return dx


class BatchNormalization:
  # http://arxiv.org/abs/1502.03167
  # y <- r(gamma)*x+b(beta)

  def __init__(self, gamma, beta, momentum=0.9, running_mean=None, running_var=None):
    self.gamma = gamma
    self.beta = beta
    self.momentum = momentum
    self.input_shape = None

    self.running_mean = running_mean
    self.running_var = running_var

    self.batch_size = None
    self.xhat = None
    self.ivar = None
    self.sqrtvar = None
    self.var = None
    self.xmu = None

  def forward(self, x, train_flg=True):
    print "%% Batch forward %%"
    print x
    self.input_shape = x.get_demension()
    if x.ndim != 2 :
      N, C, H, W = x.get_demension()
      x = x.reshape(N, reduce(lambda x, y : x*y, self.input_shape)/N)
    
    out = self.__forward(x, train_flg)
    
    print out
    return out.reshape(*self.input_shape)
  
  def __forward(self, x, train_flg) :
    if self.running_mean is None :
      self.running_mean = ve.zeros_like(x)
      self.running_var = ve.zeros_like(x)
    
    if train_flg :
      print "=========================="
      mu = ve.mean(x, axis=0)
      xmu = x - mu
      xq = xmu**2
      var = ve.mean(xq, axis=0)
      sqrtvar = ve.sqrt(var + 10e-7)
      ivar = 1 / sqrtvar
      xhat = xmu * ivar
      gammax = xhat * self.gamma
      out = gammax + self.beta

      self.var = var
      self.xhat = xhat
      self.ivar = ivar
      self.sqrtvar = sqrtvar
      self.xmu = xmu

    return out

  def backward(self, dout) :
    print "%% Batch backward %%"
    print dout
    if dout.ndim != 2:
      N, C, H, W = dout.get_demension()
      dout = dout.reshape(N, reduce(lambda x, y : x*y, dout.get_demension())/N)
    
    dx = self.__backward(dout)
    
    dx = dx.reshape(*self.input_shape)

    print dx

    return dx

  def __backward(self, dout) :
    dbeta = dout.sum(axis=0)
    dgammax = dout

    dgamma = ve.sum(ve.mul(self.xhat, dgammax), axis=0)
    dxhat = dgammax * self.gamma

    divar = ve.sum(ve.mul(dxhat, self.xmu), axis=0)
    dxmu1 = dxhat * self.ivar 
    
    dsqrtvar = divar * (1/(self.sqrtvar**2)) * (-1)
    
    dvar = (1/ve.sqrt(self.var + 10e-7)) * dsqrtvar * 0.5

    dsq = ve.arange([1 for i in range(reduce(lambda x, y : x*y, dout.get_demension()))]).reshape(dout.get_demension()) * (dvar / dout.get_demension()[1])

    dxmu2 = ve.mul(self.xmu, dsq) * 2

    dx1 = dxmu1 + dxmu2
    dmu = ve.sum(dxmu1 + dxmu2, axis=0) * (-1)

    dx2 = ve.arange([1 for i in range(reduce(lambda x, y : x*y, dout.get_demension()))]).reshape(dout.get_demension()) * (dmu / dout.get_demension()[1])

    dx = dx1 + dx2
    
    return dx
