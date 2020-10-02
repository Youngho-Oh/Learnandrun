import math

def factorial(nth):
  if nth <= 0 :
    return 1
  else :
    try :
      return nth*factorial(nth-1)
    except OverflowError :
      #print "Error : OverflowError"
      return 0
    except RuntimeError :
      #print "Error : RuntimeError"
      return 0

class natual:
  # Class valuable
  # None
  # Instance Valuable
  _e = 0.0
  _exponent = 0

  def _taylor_series(self, expo, n=0):
    if n == 0 :
      return 1.0 + self._taylor_series(expo, 1)
    try :
      temp = 1.0/factorial(n)
      #print temp
    except OverflowError :
      return 0
    try :
      result = (expo**n)*temp
    except ZeroDivisionError :
      #print "aaa"
      return 0

    return result + self._taylor_series(expo, n+1)

  def _make_natual(self, expo):
    #TODO
    return self._taylor_series(expo)

  def __init__(self, expo=1):
    if self._e == 0.0 :
      self._e = self._make_natual(expo)
      self._exponent = expo

#e = natual()
#print e._e
#print math.log(e._e)
