import usr_math as um
import vector as np

e = um.natual()._e

"""
Logical Functions
"""

def AND(x1, x2, b = -0.7):
  x = np.arange([x1, x2])
  w = np.arange([0.5, 0.5]).reshape(2,1)
  tmp = x * w + b
  if tmp <= 0 :
    return 0
  else :
    return 1

def NAND(x1, x2, b = 0.7):
  x = np.arange([x1, x2])
  w = np.arange([-0.5, -0.5]).reshape(2,1)
  tmp = x * w + b
  if tmp <= 0 :
    return 0
  else :
    return 1

def OR(x1, x2, b = -0.2):
  x = np.arange([x1, x2])
  w = np.arange([0.5, 0.5]).reshape(2,1)
  tmp = x * w + b
  if tmp <= 0 :
    return 0
  else :
    return 1

def NOR(x1, x2):
  return AND(NAND(x1, x2),OR(x1, x2))


"""
Activation Functions
"""

def _step_function(x):
  if x <= 0 :
    return 0
  else :
    return 1

def _sigmoid(x):
  global e
  return 1 / (1 + e**(-x))  

def _relu(x):
  if x <= 0 :
    return 0
  else :
    return x

def _f(func, x):
  if (type(x) == type(np.arange([1]))) and (len(x.get_demension()) >= 2) and (x.get_demension()[0] == 1) :
    #TODO
    lst = list(map(func, x.get_origin_list()))
    #print lst
    return np.arange(lst).reshape(1,len(lst))
  elif (type(x) == type(1)) or (type(x) == type(1.0)):
    return func(x)
  else :
    #print type(x)
    raise ValueError

def step_function(x):
  return _f(_step_function, x)

def sigmoid(x):
  return _f(_sigmoid, x)

def relu(x):
  return _f(_relu, x)

"""
Loss Function
"""

# XXX
"""
def _numerical_gradient(f, x):
  dmen = x.get_demension()
  tlen = reduce(lambda x, y : x*y, dmen)
  gradlst = [0 for _ in range(tlen)]

  for idx in range(tlen):
    hlst = [0 for _ in range(tlen)]
    hlst[idx] = 1e-4
    h = np.arange(hlst).reshape(dmen)
    print "<<<<<<<<<<<<<<<<<<<<!"
    print idx
    print h

    print x
    x = x+h
    print x
    fxh2 = f(x)
    print "123123123123123"
    print x
    x = x-h
    print "456456456456456"
    print x
    x = x-h
    print "789789789789789"
    print x
    fxh1 = f(x)

    gradlst[idx] = ((fxh2 - fxh1) / (1e-4 + 1e-4))

    x = x+h
    print x

    print gradlst

  grad = np.arange(gradlst).reshape(dmen)

  print grad
  print "!>>>>>>>>>>>>>>>>>>>>"

  return grad
"""

def _numerical_gradient(f, x):
  h = 1e-4
  dmen = x.get_demension()
  tlen = reduce(lambda x, y : x*y, dmen)
  grad_lst = []

  it = np.nditer(x)
  while not it.finished:
    idx = it.multi_index
    tmp_val = it.iterget(idx)
    it.iterset(idx, ((tmp_val * 1.0) + h))
    print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print x
    fxh1 = f(x)

    it.iterset(idx, ((tmp_val * 1.0) - h))
    print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print x
    fxh2 = f(x)
    grad_lst.append((fxh1 - fxh2) / (2 * h))
    #grad_lst[it._get_cur_ptr(list(idx))] = (fxh1 - fxh2) / (2 * h)
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print it._get_cur_ptr(list(idx))
    print grad_lst
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    it.iterset(idx, tmp_val)
    it.iternext()

  grad = np.arange(grad_lst).reshape(dmen)

  print grad
  print "!>>>>>>>>>>>>>>>>>>>>>"

  return grad

def gradient_descent(f, init_x, lr=0.01, step_num=100):
  x = init_x

  for i in range(step_num):
    grad = _numerical_gradient(f, x)
    x = x - (grad * lr)

  return x
