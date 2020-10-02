import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from lib import perceptron as pe
from lib import vector as np
from lib import layer as la
from lib import loss as lo
from lib import layer_naive as ln
import random
import collections

class TwoLayerNet:
  def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
    self.params = {}
    self.params['W1'] = np.arange([0.1*random.randint(1,9) for _ in range(input_size*hidden_size)]).reshape(input_size, hidden_size)
    self.params['b1'] = np.arange([0.1*random.randint(1,9) for _ in range(hidden_size)]).reshape(1, hidden_size)
    self.params['W2'] = np.arange([0.1*random.randint(1,9) for _ in range(hidden_size*output_size)]).reshape(hidden_size, output_size)
    self.params['b2'] = np.arange([0.1*random.randint(1,9) for _ in range(output_size)]).reshape(1, output_size)

    self.layers = collections.OrderedDict()
    self.layers['Affine1'] = ln.Affine(self.params['W1'], self.params['b1'])
    self.layers['Relu1'] = ln.Relu()
    self.layers['Affine2'] = ln.Affine(self.params['W2'], self.params['b2'])

    self.lastlayer = ln.SoftmaxWithLoss()

  def predict(self, x):
    for layer in self.layers.values():
      x = layer.forward(x)
    return x

  def loss(self, x, t):
    print "<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    print x
    y = self.predict(x)

    print y
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>"

    return self.lastlayer.forward(y, t)

  def accuracy(self, x, t):
    y = self.predict(x)
    y = np.argmax(y, axis=1)
    if t.ndim != 1 : t = np.argmax(t, axis=1)

    accuracy = np.sum(y == t) / float(x.shape[0])
    return accuracy

  def numerical_gradient(self, x, t):
    loss_W = lambda W: self.loss(x, t)

    grads = {}
    grads['W1'] = pe._numerical_gradient(loss_W, self.params['W1'])
    grads['b1'] = pe._numerical_gradient(loss_W, self.params['b1'])
    grads['W2'] = pe._numerical_gradient(loss_W, self.params['W2'])
    grads['b2'] = pe._numerical_gradient(loss_W, self.params['b2'])
    
    print "forwards"
    print grads['W1']
    print grads['b1']
    print grads['W2']
    print grads['b2']

    return grads

  def gradient(self, x, t):
    self.loss(x, t)

    dout = 1
    dout = self.lastlayer.backward(dout)

    layers = list(self.layers.values())
    layers.reverse()
    for layer in layers:
      #print layer
      dout = layer.backward(dout)

    grads = {}
    grads['W1'] = self.layers['Affine1'].dW
    grads['b1'] = self.layers['Affine1'].db
    grads['W2'] = self.layers['Affine2'].dW
    grads['b2'] = self.layers['Affine2'].db

    print "backwards"
    print grads['W1']
    print grads['b1']
    print grads['W2']
    print grads['b2']

    return grads

#TODO
#a = [1,2,3,4,5,6,7,8]
#x = np.arange(a).reshape(2,4)
#dmen = x.get_demension()
#y = x.reshape(1, reduce(lambda x,y : x*y, x.get_demension()))
#print y
#z = np.arange(np.exp(y)).reshape(dmen)
#print z

#x = np.arange(a)
#y = np.arange(a).reshape(8,1)
#z = x * y
#r = y * x
#print x
#print y
#print z
#print r

