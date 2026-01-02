import math
import numpy as np
from functools import reduce


def spaceinput():
    return list(map(int,input().split(" ")))


def _gcd(*numbers):
    return reduce(math.gcd, numbers)

#def gcd(numbers):
#    return reduce(np.gcd, numbers)

def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)


def gcd_n(numbers):
  '''Returns GCD of given n numbers.
  Argument: numbers - List of given numbers
  '''
  return reduce(lambda x, y: gcd(x, y), numbers)



N,X=spaceinput()

x=spaceinput()

x.append(X)
x=sorted(x)
d=[]
for i,xx in enumerate(x[:-1]):
    d.append(x[i+1]-x[i])

#print(d)

#print( np.gcd(12, 20))
print(gcd_n(d))