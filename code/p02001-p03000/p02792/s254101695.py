from itertools import product
from functools import reduce
import operator
def prod(iterable):
    return reduce(operator.mul, iterable, 1)
def cnt_samelen(b,e,n_str):
  n0=int(n_str[0])
  if b>n0 or len(n_str)==1:
    return 0
  if b<n0:
    return b*int(10**(len(n_str)-2))
  
  return (int(n_str[1:-1])+1 if len(n_str)>2 else 1)-(1 if e>int(n_str[-1]) else 0)
def cnt(b,e,n_str):
  res=0
  l=len(n_str)
  if b==e and int(n_str)>=b:
    res+=1
  for i in range(l-2):
    res+=10**(i)
  res+=cnt_samelen(b,e,n_str)
  return res
def sol():
  n_str=input()
  return sum(cnt(b,e,n_str)*cnt(e,b,n_str) 
             for b,e in product(range(1,10),repeat=2))

print(sol())  