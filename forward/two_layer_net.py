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

    #backward
    self.layers = collections.OrderedDict()
    self.layers['Affine1'] = ln.Affine(self.params['W1'], self.params['b1'])
    self.layers['Relu1'] = ln.Relu()
    self.layers['Affine2'] = ln.Affine(self.params['W2'], self.params['b2'])

    self.lastlayer = ln.SoftmaxWithLoss()

  def predict(self, x):
    #backward
    for layer in self.layers.values():
      x = layer.forward(x)

    return x

  #forward
  #def predict(self, x, t):
    #W1, W2 = self.params['W1'], self.params['W2']
    #b1, b2 = self.params['b1'], self.params['b2']

    #print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    #a1 = x * W1 + b1
    #print a1.get_origin_list()
    #z1 = pe.sigmoid(a1)
    #a2 = z1 * W2 + b2
    #print a2.get_origin_list()
    #y = la.softmax(la._classification, a2)
    #print y
    #print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    #return y

  def loss(self, x, t):
    y = self.predict(x)
    return self.lastlayer.forward(y, t)

  #forward
  #def loss(self, x, t): 
    #y = self.predict(x, t)

    #print lo.cross_entropy_error(y, t)
    #return lo.cross_entropy_error(y, t)

  def accuracy(self, x, t):
    y = self.predict(x)
    #TODO

  def numerical_gradient(self, x, t):
    loss_W = lambda W: self.loss(x, t)

    grads = {}
    grads['W1'] = pe._numerical_gradient(loss_W, self.params['W1'])
    #print grads['W1']
    grads['b1'] = pe._numerical_gradient(loss_W, self.params['b1'])
    #print grads['b1']
    grads['W2'] = pe._numerical_gradient(loss_W, self.params['W2'])
    #print grads['W2']
    grads['b2'] = pe._numerical_gradient(loss_W, self.params['b2'])
    #print grads['b2']

    return grads

  #backward
  def gradient(self, x, t):
    self.loss(x, t)

    dout = 1
    dout = self.lastLayer.backward(dout)

    layers = list(self.layers.values())
    layers.reverse()
    for layer in layers:
      dout = layer.backward(dout)

    grads = {}
    grads['W1'] = self.layers['Affine1'].dW
    grads['b1'] = self.layers['Affine1'].db
    grads['W2'] = self.layers['Affine2'].dW
    grads['b2'] = self.layers['Affine2'].db

    return grads
