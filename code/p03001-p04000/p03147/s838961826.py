import numpy as np
n = int(input())
h0 = [int(i) for i in input().split()]
h = np.zeros(n,dtype = int)
x = np.zeros(n,dtype = int)
#最小値
def minh(h,x):
  tmp1 = 100
  for i in range(n):
    if x[i] == 0:
      if h0[i] <= tmp1:
        tmp1 = h0[i]
  return tmp1
#水やり
def mizu(h,x,tmp):
  for i in range(n):
    if x[i] == 0:
      h[i] = tmp
    if h0[i] == tmp:
      x[i] = 1
#分割数
def bunnkatu(x):
  for i in range(n):
    if i == 0:
      if x[i] == 0:
        s = 1
      else:
        s = 0
    else:
      if x[i] == 0 and x[i-1] == 1:
        s += 1
  return s

def main():
  tmp = min(h0)
  ans = tmp
  mizu(h,x,tmp)
  while tmp < max(h0):
    tmp0 = minh(h,x)
    s = bunnkatu(x)
    mizu(h,x,tmp0)
    ans += s*(tmp0 - tmp)
    tmp = tmp0
  return ans

ans = main()
print(ans)