#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)

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

from decimal import Decimal

a,b,x = II()

p = x*(math.ceil(Decimal(a)/Decimal(x)))
q = x*(math.floor(Decimal(b)/Decimal(x)))

if p>b or q<a or p>q:
  print(0)
else:
  print((q-p)//x+1)