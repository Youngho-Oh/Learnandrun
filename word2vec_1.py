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


# sample context data
c0 = np.arange([1, 0, 0, 0, 0, 0, 0])
c1 = np.arange([0, 0, 1, 0, 0, 0, 0])

W_in = np.random.randn(7,3)
W_out = np.random.randn(3,7)


in_layer0 = ln.MatMul(W_in)
in_layer1 = ln.MatMul(W_in)
out_layer = ln.MatMul(W_out)

h0 = in_layer0.forward(c0)
h1 = in_layer1.forward(c1)
h = (h0 + h1) * 0.5
s = out_layer.forward(h)

print s

#print a
#print(np.mean(a, axis=0))
#print(np.mean(a, axis=1))

#b = np.random.randn(2,3)
#print b

#print "======================================="
# Xavier init valuable
#node_num = 5
#c = np.random.randn_xavier(node_num, node_num)
#print c

#print "======================================"
#d = np.random.randn_he(node_num, node_num)
#print d
