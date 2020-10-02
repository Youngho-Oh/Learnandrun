import copy
import usr_math as um
import random as rd
import math

e = um.natual()._e

class arange:
  # Class Valuable
  # None
  # Instance Valuable 
  _origin_list = None
  _demension = None
  ndim = None

  def _make_one_demension_list(self, list):
    if (type(list) == type(1)) or (type(list) == type(1.0)):
      return [list]
    elif type(reduce(lambda x, y : x+y, list)) != type([]):
      return list

    return self._make_one_demension_list(reduce(lambda x, y : x + y, list))

  def _divide_list(self, list, column=2):
    return [list[i*column:(i+1)*column] for i in range((len(list)+column-1)//column)]

  def _make_multi_demension_list(self, list, demension):
    if len(demension) == 0 :
      return list[0]

    div = demension[len(demension)-1]
    if div != 1 :
      list = self._divide_list(list, div)
    
    return self._make_multi_demension_list(list, demension[0:len(demension)-1])

  def _check_demension(self):
    self.ndim = 1
    
    for i in range(1, len(self._demension)):
      if int(self._demension[i]) > 1 :
        self.ndim += 1

  def _make_demension(self, *args):
    if len(args) == 0:
      return

    self._demension.append(args[0])
    if len(args) == 1:
      self._check_demension()
    elif len(args) == 2:
      self._make_demension(args[1])
    elif len(args) > 2:
      self._make_demension(args[1:])

  def __init__(self, n):
    self._origin_list = []
    self._demension = []
    self.ndim = 0

    if type(n) == type(1) :
      #print "ccc"
      if len(self._origin_list) == 0 :
        for i in range(1,n+1):
          self._origin_list.append(i)
        self._make_demension(1,n)
        #print "ddd"
    elif type(n) == type([]) :
      #TODO
      self._origin_list = copy.deepcopy(n)
      self._make_demension(1,len(n))
      #print len(n)

  #def __repr__(self):
    #return self

  def __str__(self):
    return str(self._origin_list)

  def reshape(self, *args):
    if len(args) == 1 :
      args = tuple(args[0])

    if reduce(lambda x, y : x*y, self._demension) == reduce(lambda x, y : x*y, args):
      self._origin_list = self._make_one_demension_list(self._origin_list)
      #self._make_demension(args)
      self._demension = list(map(int, args))
      self._origin_list =  self._make_multi_demension_list(self._origin_list, self._demension)
      self._check_demension()
    else :
      print self._origin_list
      print self._demension
      raise ValueError

    return self

  def get_demension(self):
    return self._demension

  def get_origin_list(self):
    return self._origin_list

  def _transpose(self, demension, pos):
    axis_1st = demension[0]
    axis_2nd = demension[1]

    cur_1st = pos / axis_2nd
    cur_2nd = pos % axis_2nd

    after_pos = cur_2nd * axis_1st + cur_1st

    return after_pos

  def transpose(self):
    target = self._make_one_demension_list(self._origin_list)
    result = [0 for _ in range(len(target))]

    for i in range(0, len(target)):
      ptr = self._transpose(self._demension, i)
      result[ptr] = target[i]
    
    return arange(result).reshape(self._demension[1], self._demension[0])

  def __add__(self, other):
    if (type(other) != type(1)) and (type(other) != type(1.0)) and (type(other) != type(arange([2]))) :
      raise ValueError

    #sum = arange(self._make_one_demension_list(self.get_origin_list()))
    a = self._make_one_demension_list(self.get_origin_list())
    out = []

    if type(other) == type(arange([2])) :
      if self.get_demension() != other.get_demension() :
        raise ValueError

      b = other._make_one_demension_list(other.get_origin_list())

      for i in range(0,len(a)):
        out.append(a[i]+b[i])
        #a[i] = a[i]+b[i]
    else :
      for i in range(0,len(a)):
        out.append(a[i]+other)
        #a[i] = a[i]+other

    self._origin_list = self._make_multi_demension_list(a, self.get_demension())

    #print "-=-=-=-=-=-=-=-=-=-=-=-="
    #print self._origin_list
    #print self._demension
    #print other

    return arange(out).reshape(self.get_demension())
    #return self

  def __sub__(self, other):
    if (type(other) != type(1)) and (type(other) != type(1.0)) and (type(other) != type(arange([2]))) :
      print "1111"
      print type(other)
      raise ValueError

    #sub = arange(self._make_one_demension_list(self.get_origin_list()))
    a = self._make_one_demension_list(self.get_origin_list())
    out = []

    if type(other) == type(arange([2])) :
      if self.get_demension() != other.get_demension() :
        print "2222"
        print self.get_demension()
        print other.get_demension()
        raise ValueError

      b = other._make_one_demension_list(other.get_origin_list())

      for i in range(0,len(a)):
        out.append(a[i]-b[i])
        #a[i] = a[i]-b[i]
    else :
      for i in range(0,len(a)):
        out.append(a[i]-other)
        #a[i] = a[i]-other

    self._origin_list = self._make_multi_demension_list(a, self.get_demension())
    #sub._demension = self.get_demension()

    #print "+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_"
    #print self._origin_list
    #print self._demension
    #print other

    return arange(out).reshape(self.get_demension())
    #return self

  def __mul__(self, other):
    #print "&&&&&&&&&&&&&"
    if type(other) == type(1) or type(other) == type(1.0) :
      #print "__mul__ : ******************"
      dmen = self.get_demension()
      mul = arange(self._make_one_demension_list(self.get_origin_list()))
      a = mul.get_origin_list()
      b = [other for _ in range(len(a))]
      #print a
      #print b
      #print "__mul__"
           
      for i in range(0,len(a)):
        a[i] = a[i]*b[i]

      #mul._origin_list = mul._make_multi_demension_list(mul.get_origin_list(), self.get_demension())
      #mul.demension = copy.deepcopy(self.get_demension())
      mul.reshape(dmen)
    elif (len(self.get_demension()) == 2) and (type(other) == type(arange(2))) and (len(other.get_demension()) == 2) and (self.get_demension()[1] == other.get_demension()[0]) :
      #print "vector"
      data = []
      a_row = self.get_demension()[0]
      a_column = self.get_demension()[1]
      a = self._make_one_demension_list(self.get_origin_list())
      #print "a_row : "
      #print a_row
      #print "a_column : "
      #print a_column
      #other.transpose(0,1)
      #xxx
      #other.transpose()
      b_row = other.get_demension()[0]
      b_column = other.get_demension()[1]
      b = other._make_one_demension_list(other.get_origin_list())
      #print "b_row : "
      #print b_row
      #print "b_column : "
      #print b_column

      temp = 0
      
      for i in range(0, a_row):
        for j in range(0, b_column):
          for k in range(0, a_column):
            #print a_row*i+k
            #print b_column*k+j
            #print "***********"
            try :
              #temp += a[(a_row*i)+k]*b[(b_column*k)+i]
              temp += a[(a_column*i)+k]*b[(b_column*k)+j]
            except :
              print i
              print j
              print k
              raise ValueError
            if k == (a_column-1) :
              #print temp
              data.append(temp)
              temp = 0

      #other.transpose(0,1)
      #xxx
      #other.transpose()
      #print data
      #print type(data)
      
      return arange(data).reshape(a_row, b_column)
    else:
      raise ValueError

    return mul

  def __div__(self, other):
    dmen = self.get_demension()
    out_list = []
    t_list = self.reshape(1, reduce(lambda x, y : x*y, dmen)).get_origin_list()
    total = len(t_list)
    other_list = None

    if type(other) == type(1) or type(other) == type(1.0) :
      other_list = [(other * 1.0) for _ in range(total)]
    elif (type(other) == type(arange([0]))) and (dmen == other.get_demension()) :
      other_list = other.reshape(1, reduce(lambda x, y : x*y, dmen)).get_origin_list()
    else :
      raise ValueError

    for i in range(0, total) :
      out_list.append((t_list[i]*1.0)/(other_list[i]*1.0))

    out = arange(out_list).reshape(dmen)
    self.reshape(dmen)

    if type(other) == type(arange([0])) :
      other.reshape(dmen)

    return out

  def __pow__(self, other) :
    if (type(other) != type(1)) and (type(other) != type(1.0)) :
      print "1111"
      print type(other)
      raise ValueError

    out = []
    a = self._make_one_demension_list(self.get_origin_list())

    for i in range(0,len(a)):
      out.append((a[i]*1.0)**other)

    self._origin_list = self._make_multi_demension_list(a, self.get_demension())

    return arange(out).reshape(self.get_demension())

  def sum(self, axis=None):
    a = []
    dmen = self.get_demension()
    after_dmen = 0
    del_dmen = 0
    t = self.reshape(1, reduce(lambda x, y : x*y, dmen)).get_origin_list()
    temp_sum = 0

    if (axis == None) or ((axis == 0) and (self.ndim == 2) and (dmen[0] == 1)) :
      #a.append(sum(t))
      #return a
      return sum(t)
    elif (axis == 0) and (self.ndim >= 2) :
      del_dmen = dmen.pop(0)
      temp = reduce(lambda x, y : x*y, dmen)
      for i in range(0, temp) :
        for j in range(i, len(t), del_dmen) :
          temp_sum += t[j]
        a.append(temp_sum)
        temp_sum = 0
      
      if len(dmen) == 1 :
        dmen = [1] + dmen
      self._demension = dmen
      self._origin_list = self._make_multi_demension_list(a, self.get_demension())
    #elif (axis == 1) and (self.ndim >= 2) :
      #TODO
    #elif (axis == 2) and (self.ndim >= 3)  :
      #TODO
    else :
      raise ValueError

    return self

class random :
  @classmethod
  def rand(self, *args) :
    dmen = []
    dlen = 1

    if (len(args) == 1) :
      dmen.append(1)

    for i in range(0, len(args)) :
      dlen *= args[i]
      dmen.append(args[i])
    
    data = []

    for i in range(0, dlen):
      data.append(rd.random())
    
    return arange(data).reshape(dmen)

  @classmethod
  def randn(self, *args) :
    dmen = []
    dlen = 1

    if (len(args) == 1) :
      dmen.append(1)

    for i in range(0, len(args)) :
      dlen *= args[i]
      dmen.append(args[i])

    data = []

    for i in range(0, dlen):
      data.append(rd.gauss(0.0, 1.0))

    return arange(data).reshape(dmen)

  @classmethod
  def randn_xavier(self, *args) :
    dmen = []
    input_dmen = args[0]
    output_dmen = args[len(args)-1]
    dlen = 1

    if (len(args) == 1) :
      dmen.append(1)
      input_dmen = 1

    for i in range(0, len(args)) :
      dlen *= args[i]
      dmen.append(args[i])

    data = []

    for i in range(0, dlen):
      data.append(rd.gauss(0.0, 1.0) / math.sqrt(input_dmen))
     
    return arange(data).reshape(dmen)

  @classmethod
  def randn_he(self, *args) :
    dmen = []
    input_dmen = args[0]
    output_dmen = args[len(args)-1]
    dlen = 1

    if (len(args) == 1) :
      dmen.append(1)
      input_dmen = 1

    for i in range(0, len(args)) :
      dlen *= args[i]
      dmen.append(args[i])

    data = []

    for i in range(0, dlen):
      data.append(rd.gauss(0.0, 1.0) / math.sqrt(input_dmen/2))

    return arange(data).reshape(dmen)

""" Global Functions """

def identity(n):
  lst = []

  for i in range(0, n):
    for j in range(0, n):
      if i == j:
        lst.append(1)
      else:
        lst.append(0)

  return arange(lst).reshape(n, n)

def _num_like(x, i=0):
  if type(x) != type(arange([1])):
    raise ValueError
  elif (type(x) == type(arange([1]))) and (len(x.get_demension()) != 2):
    raise ValueError
  else:
    lst = [i for _ in range(x.get_demension()[0]*x.get_demension()[1])]

    return arange(lst).reshape(x.get_demension()[0], x.get_demension()[1])

def zeros_like(x):
  return _num_like(x)

def function(f, x):
  if type(x) != type(arange([1])):
    raise ValueError
  elif (type(x) == type(arange([1]))) and (len(x.get_demension()) != 2):
    raise ValueError
  else:
    return f(x)
    #lst = x._make_one_demension_list(x.get_origin_list())
    
    #for i in range(0, len(lst)):
      #lst[i] = f(lst[i])

    #return arange(lst).reshape(x.get_demension()[0], x.get_demension()[1])

def argmax(target, axis=0):
  if axis < 0 :
    raise ValueError
  demension = target.get_demension()
  if len(demension) == 1 :
    raise ValueError
  elif len(demension) == 2 :
    if demension[0] == 1 :
      if axis >= 1 :
        raise ValueError
      else :
        a = []
        t = target.get_origin_list()
        a.append(t.index(max(t)))
        return arange(a)
    else :
      if axis == 0 :
        a = []
        trans = target.transpose()
        t = trans.get_origin_list()
        for i in range(0,int(trans.get_demension()[0])) :
          a.append(t[i].index(max(t[i])))
        return arange(a)
      elif axis == 1 :
        a = []
        t = target.get_origin_list()
        for i in range(0,int(demension[0])) :
          a.append(t[i].index(max(t[i])))
        return arange(a)
      else :
        raise ValueError
  elif len(demension) >= 3 :
    raise ValueError
  else :
    raise ValueError

def max(target, axis=None):
  if type(target) == type([]) :
    t_list = target
  else :
    t_list = target.get_origin_list()

  temp_max = 0
  temp = 0

  for i in t_list:
    if type(i) == type([]) :
      temp = max(i)
    else :
      temp = i
    
    if temp > temp_max :
      temp_max = temp

  return temp_max

def exp(target):
  if type(target) == type([]) :
    t_list = target
  else :
    t_list = target.get_origin_list()

  temp_list = []

  for i in t_list:
    if type(i) == type([]) :
      temp_list.append(exp(i))
    else :
      temp_list.append(e**(i*1.0))
  
  return temp_list

def mean(target, axis=None):
  t_list = None
  dmen = None

  if axis is None :
    dmen = target.get_demension()
    t_list = target.reshape(1, reduce(lambda x, y : x*y, dmen)).get_origin_list()
    total = len(t_list)
    out = reduce(lambda x, y : x+y, t_list) / total
    target.reshape(dmen)
  else :
    if axis == 0 :
      target.transpose().get_origin_list()
      dmen = target.get_demension()
    else :
      target.get_origin_list()
      dmen = target.get_demension()

    term = dmen[1]
    t_list = target.reshape(1, reduce(lambda x, y : x*y, dmen)).get_origin_list()

    out_list = []
    mean = 0

    for i in range(0, len(t_list)):
      mean += (t_list[i] * 1.0)
      if (i != 0) and (i % (term-1) == 0) :
         mean = mean / term
         out_list.append(mean)
         mean = 0

    target.reshape(dmen)
    if axis == 0 :
      target.transpose()

    if len(out_list) == 1 :
      out = out_list[0]
    else :
      out = arange(out_list)

  return out

def sqrt(target) :
  if type(target) == type(arange([1])) :
    dmen = target.get_demension()
    t_list = target.reshape(1, reduce(lambda x, y : x*y, dmen)).get_origin_list()
    total = len(t_list)
    out_list = []

    for i in range(0, total) :
      out_list.append(math.sqrt(t_list[i] * 1.0))

    out = arange(out_list).reshape(dmen)
    target.reshape(dmen)
  else :
    out = math.sqrt(target)

  return out

def sum(target, axis=None):
  out = None

  if type(target) == type(arange([1])) :
    a = []
    dmen = target.get_demension()
    after_dmen = 0
    del_dmen = 0
    t = target.reshape(1, reduce(lambda x, y : x*y, dmen)).get_origin_list()
    temp_sum = 0

    if (axis == None) or ((axis == 0) and (target.ndim == 2) and (dmen[0] == 1)) :
      #a.append(sum(t))
      target.reshape(dmen)
      #return a
      return sum(t)
    elif (axis == 0) and (target.ndim >= 2) :
      del_dmen = dmen.pop(0)
      temp = reduce(lambda x, y : x*y, dmen)
      for i in range(0, temp) :
        for j in range(i, len(t), del_dmen) :
          temp_sum += t[j]
        a.append(temp_sum)
        temp_sum = 0
      
      if len(dmen) == 1 :
        dmen = [1] + dmen
      out = arange(a).reshape(dmen)
      if len(dmen) == 2 and dmen[0] == 1 :
        dmen.pop(0)

      dmen = [del_dmen] + dmen
      target.reshape(dmen)

    #elif (axis == 1) and (self.ndim >= 2) :
      #TODO
    #elif (axis == 2) and (self.ndim >= 3)  :
      #TODO
    else :
      raise ValueError
  elif type(target) == type([]) :
    out = 0
    for i in range(0, len(target)) :
      out += target[i]

  return out

def mul(target1, target2) :
  out = None
  out_lst = []

  if ((type(target1) == type(1.0)) or (type(target1) == type(1))) and (type(target2) == type(arange([0]))) :
    out = target2 * target1
  elif ((type(target2) == type(1.0)) or (type(target2) == type(1))) and (type(target1) == type(arange([0]))) :
    out = target1 * target2
  else :
    if target1.get_demension() == target2.get_demension() :
      dmen = target1.get_demension()

      t1_lst = target1.reshape(1, reduce(lambda x, y : x*y, dmen)).get_origin_list()
      t2_lst = target2.reshape(1, reduce(lambda x, y : x*y, dmen)).get_origin_list()

      for i in range(0, len(t1_lst)) :
        out_lst.append(t1_lst[i]*t2_lst[i])

      target1.reshape(dmen)
      target2.reshape(dmen)

      out = arange(out_lst).reshape(dmen)
  return out


class nditer:
  target = None
  finished = False
  dmen = None
  multi_index = None
  now_ptr = None

  def _get_cur_dmen(self, ptr):
    lst = []
    
    for i in range(1, len(self.dmen)):
      lst.append(ptr / reduce(lambda x, y : x*y, self.dmen[i:]))
      ptr = ptr % reduce(lambda x, y : x*y, self.dmen[i:])

    lst.append(ptr)
    
    return lst

  def _get_cur_ptr(self, dmen):
    ptr = 0

    for i in range(0, len(dmen)):
      if i == len(dmen)-1 : ptr += dmen[i]
      else : ptr += (dmen[i] * reduce(lambda x, y : x*y, self.dmen[i+1:]))

    return ptr

  def __init__(self, n):
    self.target = n
    self.dmen = self.target.get_demension()
    self.finished = False
    self.now_ptr = 0
    self.multi_index = tuple(self._get_cur_dmen(self.now_ptr))

  def iterget(self, n):
    print n
    print self.dmen
    ptr = self._get_cur_ptr(list(n))
    self.target.reshape(1, reduce(lambda x, y : x*y, self.dmen))
    print ptr
    data = self.target.get_origin_list()[ptr]
    self.target.reshape(self.dmen)

    return data

  def iterset(self, n, d):
    ptr = self._get_cur_ptr(list(n))
    self.target.reshape(1, reduce(lambda x, y : x*y, self.dmen))
    self.target.get_origin_list()[ptr] = d
    self.target.reshape(self.dmen)

  def iternext(self) :
    self.now_ptr += 1
    if self.now_ptr >= reduce(lambda x, y : x*y, self.dmen):
      self.finished = True
      return
    self.multi_index = tuple(self._get_cur_dmen(self.now_ptr))
