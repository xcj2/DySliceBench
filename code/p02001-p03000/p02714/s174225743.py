import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
  return list(map(int,input().split()))
def m(): #複数文字
  return map(int,input().split())
def onem(): #Nとかの取得
  return int(input())
def s(x): #圧縮
  a = []
  if len(x) == 0:
    return []
  aa = x[0]
  su = 1
  for i in range(len(x)-1):
    if aa != x[i+1]:
      a.append([aa,su])
      aa = x[i+1]
      su = 1
    else:
      su += 1
  a.append([aa,su])
  return a
def jo(x): #listをスペースごとに分ける
  return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
  return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

import fractions
from functools import reduce
def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

n = onem()

s = input()[:-1]

R = [0 for _ in range(n)]
B = [0 for _ in range(n)]
G = [0 for _ in range(n)]

co = 0

if s[0] == "R":
  R[0] = 1
elif s[0] == "G":
  G[0] = 1
else:
  B[0] = 1

for i in range(1,n):
  if s[i] == "R":
    R[i] += 1
  elif s[i] == "G":
    G[i] += 1
  else:
    B[i] += 1
  R[i] += R[i-1]
  G[i] += G[i-1]
  B[i] += B[i-1]

for i in range(1,n-1):
  if s[i] == "G":
    for j in range(i):
      if s[j] == "R":
        un = (1 if (i + (i-j) < n) and s[i + (i - j)] == "B" else 0)
        co += B[-1] - B[i] - un
      elif s[j] == "B":
        un = (1 if (i + (i-j) < n) and s[i + (i - j)] == "R" else 0)
        co += R[-1] - R[i] - un

  elif s[i] == "R":
    for j in range(i):
      if s[j] == "G":
        un = (1 if (i + (i-j) < n) and s[i + (i - j)] == "B" else 0)
        co += B[-1] - B[i] - un
      elif s[j] == "B":
        un = (1 if (i + (i-j) < n) and s[i + (i - j)] == "G" else 0)
        co += G[-1] - G[i] - un

  elif s[i] == "B":
    for j in range(i):
      if s[j] == "G":
          un = (1 if (i + (i-j) < n) and s[i + (i - j)] == "R" else 0)
          co += R[-1] - R[i] - un
      elif s[j] == "R":
          un = (1 if (i + (i-j) < n) and s[i + (i - j)] == "G" else 0)
          co += G[-1] - G[i] - un
    
print(co)



