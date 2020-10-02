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
  layers['Sigmoid1'] = ln.Sigmoid()
  layers['Affine2'] = ln.Affine(network['W2'], network['b2'])
  layers['Sigmoid2'] = ln.Sigmoid()
  layers['Affine3'] = ln.Affine(network['W3'], network['b3'])

  return layers

b = np.arange([2,8,9,16]).reshape(2,2)
a = np.arange([1,2,3,4,5,6,7,8]).reshape(2,4)

print a.ndim
a.reshape(2,2,2)
print a.ndim

print "1111111111111"
print a
print a.ndim
print "3333333333333"
#print a.sum(axis=0)
print np.sum(a, axis=0)
print a.ndim
print "2222222222222"
print a
print a.ndim

#print b
#print a
#print b / a
#print b
#print a

#print a
#print(np.mean(a, axis=0))
#print(np.mean(a, axis=1))

#print a
#print np.sqrt(a)
#print a


z = np.arange([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]).reshape(1,2,2,2)

N, C, H, W = z.get_demension()

print N
print C
print H
print W


a = np.random.rand(2,3)
print a
print "======================================="
b = np.random.randn(2,3)
print b

print "======================================="
# Xavier init valuable
node_num = 5
c = np.random.randn_xavier(node_num, node_num)
print c

print "======================================"
d = np.random.randn_he(node_num, node_num)
print d
