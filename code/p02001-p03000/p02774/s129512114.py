#!/usr/bin/python3
# -*- coding:utf-8 -*-

MAX = 10**18
MIN = -MAX

def main():
  n, k = map(int, input().strip().split())
  As = list(map(int, input().strip().split()))
  As.sort()

  Ans, Aps, Azs = [], [], []
  for A in As:
    if A > 0:
      Aps.append(A)
    elif A == 0:
      Azs.append(A)
    else:
      Ans.append(A)

  def count(xs, ys, ub):
    c = 0
    r = len(ys) - 1
    for l in range(len(xs)):
      while  r >= 0 and xs[l] * ys[r] > ub:
        r -= 1
      c += r+1
    return c 

  def bs(l, r):
    while True:
      mid = (l+r) // 2
      if r - l <= 1:
        return r
      
      tot = 0      
      tot += count(Aps, Aps, mid) - sum([1 for A in Aps if A**2 <= mid])
      tot += count(Ans[::-1], Ans[::-1], mid) - sum([1 for A in Ans if A**2 <= mid])
      tot //= 2

      if mid >=0:
        tot += (len(Aps) + len(Ans)) * len(Azs) + (len(Azs) * (len(Azs) - 1)) // 2
      tot += count(Aps[::-1], Ans, mid)
      
      if tot < k:
        l = mid
      else:
        r = mid
  
  print(bs(MIN-1, MAX+1))
    
    
if __name__=='__main__':
  main()

