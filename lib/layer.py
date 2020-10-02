import perceptron as pe
import vector as ve
import usr_math as um

e = um.natual()

def init_network():
  network = {}
  network['W1'] = ve.arange([0.1, 0.3, 0.5, 0.2, 0.4, 0.6]).reshape(2,3)
  network['b1'] = ve.arange([0.1, 0.2, 0.3])
  network['W2'] = ve.arange([0.1, 0.4, 0.2, 0.5, 0.3, 0.6]).reshape(3,2)
  network['b2'] = ve.arange([0.1, 0.2])
  network['W3'] = ve.arange([0.1, 0.3, 0.2, 0.4]).reshape(2,2)
  network['b3'] = ve.arange([0.1, 0.2])

  return network

def forward(network, x):
  W1, W2, W3 = network['W1'], network['W2'], network['W3']
  b1, b2, b3 = network['b1'], network['b2'], network['b3']

  a1 = x * W1 + b1
  #print a1
  z1 = pe.sigmoid(a1)
  a2 = z1 * W2 + b2
  z2 = pe.sigmoid(a2)
  a3 = z2 * W3 + b3
  y = a3

  return y

def _regression(x):
  ident = ve.identity(x.get_demension()[1])

  return x * ident

def _classification(x):
  lst = list(map(lambda x: e._e**x, x.get_origin_list()))
  full_lst = [1 for _ in range(x.get_demension()[1])]

  a = ve.arange(lst).reshape(1, x.get_demension()[1])
  full = ve.arange(full_lst).reshape(x.get_demension()[1], 1)

  total = a * full

  #print a * (1 / total.get_origin_list())
  #print "^^^^^^^^^^^^^^^^^^^^^^^^^^^"

  return a * (1 / total.get_origin_list())


def softmax(a):
  print "=========================================="
  dmen = a.get_demension()
  c = ve.max(a)
  print c
  b = a-c
  print b
  exp_a = ve.exp(b)
  print exp_a
  y = ve.arange(exp_a).reshape(dmen)
  print y
  sum_exp_a = sum(exp_a)
  print sum_exp_a
  y = y * (1/sum_exp_a)
  print y
  print "========================================="

  return y
