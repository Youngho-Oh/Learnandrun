import two_layer_net
import random
from lib import vector as ve

x_lst = [random.uniform(0,100) for i in range(100*20)]
t_lst = [random.uniform(0,1) for i in range(100*2)]

x = ve.arange(x_lst).reshape(100,20)
t = ve.arange(t_lst).reshape(100,2)

iters_num = 1
learning_rate = 0.01
train_size = x.get_demension()[0]

network = two_layer_net.TwoLayerNet(20, 10, 2, learning_rate)

for i in range(iters_num):
  batch_mask = random.randint(0,99)

  print batch_mask

  input_lst = x.get_origin_list()[batch_mask]
  print "input"
  print input_lst
  print "===================================="
  output_lst = t.get_origin_list()[batch_mask]
  print "output"
  print output_lst
  print "==================================="

  input = ve.arange(input_lst).reshape(1,20)
  output = ve.arange(output_lst).reshape(1,2)

  grad = network.numerical_gradient(input, output)

  print grad['W1']
  print grad['b1']
  print grad['W2']
  print grad['b2']

  for key in ('W1', 'b1', 'W2', 'b2'):
    network.params[key] = network.params[key] - grad[key] * learning_rate

  print "==================================="
  print network.params['W1']
  print network.params['b1']
  print network.params['W2']
  print network.params['b2']
  print "==================================="

  loss = network.loss(input, output)
  print "===================================="
  print loss
  print "===================================="
