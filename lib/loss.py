import vector as np
import math

def _check_vector(a):
  return type(a) == type(np.arange([2]))

def mean_squared_error(y, t):
  if (_check_vector(y) == False) or (_check_vector(t) == False):
    return -1
  elif y.get_demension() != t.get_demension():
    return -1
  else:
    loss = list(map(lambda x: x**2, (y-t).get_origin_list()))
    #print loss
    return 0.5 * sum(loss)

def cross_entropy_error(y, t):
  delta = 1e-7
  if (_check_vector(y) == False) or (_check_vector(t) == False):
    return -1
  elif y.get_demension() != t.get_demension():
    return -1
  else:
    #print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    #print y.get_origin_list()
    #print t.get_origin_list()
    loss = list(map(lambda x: (x + delta), y.get_origin_list()))
    #print loss
    loss = list(map(lambda x: math.log(x), loss))
    #print loss
    rst = list(map(lambda x, y : x*y, t.get_origin_list(), loss))
    #print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    #print rst
    #print sum(rst)
    return -1 * sum(rst)
