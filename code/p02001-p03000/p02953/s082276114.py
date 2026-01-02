import os, sys
import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")
 
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10**18
MOD = 10**9 + 7

def N(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))
def bulk_li(): return list(map(lambda s: list(map(int, s.split())), sys.stdin.readlines()))

n = N()
hs = np.array(li())

hs_diff = hs[1:] - hs[:-1]
# print(hs_diff)

result = 'Yes'
flg = 0
for diff in hs_diff:
  if diff < -1:
    result = 'No'
  elif diff == -1 and flg == 1:
    result = 'No'
  elif diff == -1:
    flg = 1
  elif diff == 0 and flg == 1:
    flg = 1
  else:
    flg = 0

print(result)
