#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
  return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
  read_all = [tuple(map(int, input().split())) for _ in range(N)]
  return map(list,zip(*read_all))

#################

Q = I()
l,r = Line(Q)

def is_prime_all(n):
  is_prime = [True]*(n+1)
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, int(n**0.5+1)):
    if not is_prime[i]:
      continue
    for j in range(i*2,n+1,i):
      is_prime[j] = False
  return is_prime

prime_judge = is_prime_all(10**5)

a = []
for i in range(10**5):
  if i==0 or i==1 or i==2:
    a.append(0)
  else:
    if i%2==0:
      a.append(a[-1])
    else:
      if (prime_judge[i]==True) and (prime_judge[(i+1)//2]==True):
        a.append(a[-1]+1)
      else:
        a.append(a[-1])

for i in range(Q):
  print(a[r[i]]-a[l[i]-1])