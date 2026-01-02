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

N = I()

dig = len(str(N))
if dig==1:
  print(N)
  exit()
if dig==2:
  print(9)
  exit()
if dig==3:
  print(9+N-100+1)
  exit()
if dig==4:
  print(9+900)
  exit()
if dig==5:
  print(9+900+N-10000+1)
  exit()
if dig==6:
  print(9+900+90000)