from backward import two_layer_net
import random
from lib import vector as ve

iters_num = 1

network = two_layer_net.TwoLayerNet(input_size=4, hidden_size=4, output_size=2)

x_train = [int(random.uniform(0,100)) for i in range(4*3)]
t_train = [0,1,1,0,0,1]

x_batch = ve.arange(x_train).reshape(3,4)
t_batch = ve.arange(t_train).reshape(3,2)

for i in range(iters_num):
  print "========================="
  print i
  print "========================="
  input = x_batch.get_origin_list()[i]
  output = t_batch.get_origin_list()[i]

  x_vector = ve.arange(input)
  t_vector = ve.arange(output)

  print "**********FORWARD***************"
  print x_vector
  print t_vector

  grad_numerical = network.numerical_gradient(x_vector, t_vector)

  print "**********BACKWARD***************"
  print x_vector
  print t_vector

  grad_backprob = network.gradient(x_vector, t_vector)

  for key in grad_numerical.keys():
    diff = grad_backprob[key] - grad_numerical[key]
    print(key + ":" + str(diff))
