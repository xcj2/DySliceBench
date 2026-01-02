from itertools import *
from heapq import *

def comp(a,b):
  return all(x==y or "?" in (x,y) for x,y in zip(a, b))

def _merge_mid(a,b):
  la, lb = map(len,[a,b])
  for i in range(la-lb+1):
    if comp(a[i:],b):
      yield i

def merge_mid(a,b):
  return list(_merge_mid(a,b))

def _merge_right(a,b):
  la, lb = map(len,[a,b])
  for i in range(max(la-lb+1, 1),la):
    if comp(b, a[i-la:]):
      yield i
  yield la

def merge_right(a,b):
  return list(_merge_right(a,b))

class K(int):
  def __new__(cls, *args, **kwargs):
    cb = kwargs.pop("cb")
    i = int.__new__(cls, *args, **kwargs)
    i.cb = cb
    return i

def min_merge(a,b,c):
  keys = sorted([a,b,c],key=len,reverse=True)
  len_keys = list(map(len, keys))
  mid = {(i,j):merge_mid(keys[i],keys[j]) for i,j in permutations(range(3), 2)}
  right = {(i,j):merge_right(keys[i],keys[j]) for i,j in permutations(range(3), 2)}
  
  for i in mid[0,1]:
    for j in mid[0,2]:
      if j+len_keys[2] <= i or i+len_keys[2] <= j or j-i in mid[1,2] or j-i in right[1,2] or i-j in right[2,1]:
        return len_keys[0]
  
  def candicates(a,b,c):
    return chain(
      (K(i+len_keys[b], cb=lambda:(
       (mid[a,c] and mid[a,c][0]+len_keys[c] <= i) or (mid[b,c] and len_keys[a] <= i+mid[b,c][-1]) or 
       any((i-j in right[c,b] if i>j else j-i in mid[b,c]) for j in dropwhile((i-len_keys[c]).__gt__, mid[a,c]+right[a,c]))
      )) for i in dropwhile((len_keys[c]-len_keys[b]+1).__gt__, right[a,b])),
      (K(min(i+next(dropwhile((len_keys[a]-i+1).__gt__, y))+len_keys[b] for i in x), cb=lambda:True) for (x, y) in [sorted((right[a,c], right[c,b]), key=len)]),
    )
  
  can = merge(*(candicates(x,y,z) for x,y,z in permutations(range(3),3)))
  
  for k in can:
    if k.cb():
      return k
  
  return sum(len_keys)

a=input()
b=input()
c=input()

print(min_merge(a,b,c))

