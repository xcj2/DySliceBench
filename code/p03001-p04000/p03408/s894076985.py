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

N = I()
s = ['0']*N
for i in range(N):
  s[i] = str(input())
M = I()
t = ['0']*M
for i in range(M):
  t[i] = str(input())

from collections import Counter
sc = Counter(s)
tc = Counter(t)
ans = 0
for i in range(N):
  tmp = sc[s[i]] - tc[s[i]]
  if tmp > ans:
    ans = tmp
print(ans)