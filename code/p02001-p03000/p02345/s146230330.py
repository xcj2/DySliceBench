# -*- coding: utf-8 -*-
INF = 2**31 -1
n, p = list(map(int, input().split()))

temp = 1
while temp < n:
  temp *= 2

lis = [INF for i in range(2*temp-1)]

def updata(x, y):
  x += temp - 1
  lis[x] = y
  while x > 0:
    x = (x-1) // 2
    #print(x*2+2)
    lis[x] = min(lis[x*2+1], lis[x*2+2])

def findmin(x, y):
  return query(x, y+1, 0, 0, temp)

def query(a, b, k, l, r):
  #print('a,b,l,r:',a,b,l,r)
  if r <= a or b <= l:
    return INF

  if a <= l and r <= b:
    return lis[k]
  
  vl = query(a, b, k*2+1, l, (l+r)//2)
  vr = query(a, b, k*2+2, (l+r)//2, r)
  return min(vl, vr)


for i in range(p):
  oper, x, y = list(map(int, input().split()))
  
  if oper == 0:
    updata(x, y)
  else: 
    print(findmin(x, y))


