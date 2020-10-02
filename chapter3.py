import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from lib import perceptron as pe
from lib import vector as np
from lib import layer as la
from lib import loss as lo
from lib import layer_naive as ln
from lib import optimizer as op
import random
import collections

def init_network():
  network = {}
  network['W1'] = np.arange([0.1, 0.3, 0.5, 0.2, 0.4, 0.6]).reshape(2,3)
  network['b1'] = np.arange([0, 0, 0])
  network['W2'] = np.arange([0.1, 0.4, 0.2, 0.5, 0.3, 0.6]).reshape(3,2)
  network['b2'] = np.arange([0, 0])
  network['W3'] = np.arange([0.1, 0.3, 0.2, 0.4]).reshape(2,2)
  network['b3'] = np.arange([0, 0])

  layers = collections.OrderedDict()
  layers['Affine1'] = ln.Affine(network['W1'], network['b1'])
  layers['BatchNorm1'] = ln.BatchNormalization(gamma=1, beta=0)
  layers['Sigmoid1'] = ln.Sigmoid()
  layers['Affine2'] = ln.Affine(network['W2'], network['b2'])
  layers['BatchNorm2'] = ln.BatchNormalization(gamma=1, beta=0)
  layers['Sigmoid2'] = ln.Sigmoid()
  layers['Affine3'] = ln.Affine(network['W3'], network['b3'])

  return layers


def loss(network, x, t) :
  for layer in network :
    x = layer.forward(x)

  return ln.SoftmaxWithLoss().forward(x, t)

# MAIN

print "++++++++++++++++ FORWARD +++++++++++++++++++++++"
forward_layer = init_network()
forward_network = list(forward_layer.values())

_in = np.arange([1.5, 0.5])
_result = np.arange([1.0, 0.0])
#_result = np.arange([1.0, 0.0, 0.0])

loss_W = lambda W: loss(forward_network, _in, _result)

fw_affine1_W = pe._numerical_gradient(loss_W, forward_layer['Affine1'].W)
fw_affine1_b = pe._numerical_gradient(loss_W, forward_layer['Affine1'].b)
fw_affine2_W = pe._numerical_gradient(loss_W, forward_layer['Affine2'].W)
fw_affine2_b = pe._numerical_gradient(loss_W, forward_layer['Affine2'].b)
fw_affine3_W = pe._numerical_gradient(loss_W, forward_layer['Affine3'].W)
fw_affine3_b = pe._numerical_gradient(loss_W, forward_layer['Affine3'].b)

print "+++++++++++++++++ BACKWARD ++++++++++++++++++++++"
backward_layer = init_network()
backward_network = list(backward_layer.values())
optimizer = op.SGD()

dout = _in
for step in backward_network:
  #print step
  dout = step.forward(dout)
  #print dout

softmax = ln.SoftmaxWithLoss()
softmax.forward(dout, _result)

backward_network.reverse()

dout = softmax.backward()

for step in backward_network:
  print step
  dout = step.backward(dout)

params = {}
params['W1'], params['b1'] = backward_layer['Affine1'].W, backward_layer['Affine1'].b
params['W2'], params['b2'] = backward_layer['Affine2'].W, backward_layer['Affine2'].b
params['W3'], params['b3'] = backward_layer['Affine3'].W, backward_layer['Affine3'].b

grads = {}
grads['W1'], grads['b1'] = backward_layer['Affine1'].dW, backward_layer['Affine1'].db
grads['W2'], grads['b2'] = backward_layer['Affine2'].dW, backward_layer['Affine2'].db
grads['W3'], grads['b3'] = backward_layer['Affine3'].dW, backward_layer['Affine3'].db

print "+++++++++++++++++++++ result +++++++++++++++++++++++++"
print backward_layer['Affine1'].dW - fw_affine1_W
print backward_layer['Affine1'].db - fw_affine1_b
print backward_layer['Affine2'].dW - fw_affine2_W
print backward_layer['Affine2'].db - fw_affine2_b
print backward_layer['Affine3'].dW - fw_affine3_W
print backward_layer['Affine3'].db - fw_affine3_b

#print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
#print backward_layer['Affine1'].W
#print backward_layer['Affine1'].b
#print backward_layer['Affine2'].W
#print backward_layer['Affine2'].b
#print backward_layer['Affine3'].W
#print backward_layer['Affine3'].b
#optimizer.update(params, grads)
#print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
#print backward_layer['Affine1'].W
#print backward_layer['Affine1'].b
#print backward_layer['Affine2'].W
#print backward_layer['Affine2'].b
#print backward_layer['Affine3'].W
#print backward_layer['Affine3'].b
