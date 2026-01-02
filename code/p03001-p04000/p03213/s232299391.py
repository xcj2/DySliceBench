# /user/bin/python
# -*- coding: utf-8 -*-
import sys 


N = int(input())

def fact(e, n):
  i = 2
  while(n > 1 and i <= n):
    if n % i == 0:
      n //= i
      if i in e:
        e[i] += 1
      else:
        e[i] = 1
    else:
      i += 1

def cnt75(elem_v, elem_75):
  ans = 1
  for i in range(len(elem_75)):
    n = 0
    for j in elem_v:
      if j >= elem_75[i]:
        n += 1
    ans *= (n-i)
  return ans    

def cnt75_2(elem_v):
  ans = 1
  n = 0
  m = 0
  for i in elem_v:
    if i >= 4:
      n += 1
    if i >= 2:
      m += 1
  return n*(n-1)//2 * (m-2)

elem = {}
for n in range(2, N+1):
  fact(elem, n)
elem_v = sorted(elem.values())

ans = cnt75(elem_v,[74])
ans += cnt75(elem_v,[24,2])
ans += cnt75(elem_v,[14,4])
ans += cnt75_2(elem_v)

print(ans)