import sys, array, re, functools
from math import sqrt, ceil; from itertools import count, islice
input = lambda: sys.stdin.readline()
@functools.lru_cache(maxsize = 10000)



def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
def f(a, b):
  return  max(len(str(a)), len(str(b)))

def Main():
  N = int(input())
  v = -1
  if isPrime(N):
    print(len(str(N)))
  elif not isPrime(N):
    for i in range(1, ceil(sqrt(N)) + 1):
      if N%i == 0:
        t = f(int(i), int (N/i))
        if v == -1 or v > t:
          v = t
    print(v)
    
if __name__ == '__main__':
  Main()