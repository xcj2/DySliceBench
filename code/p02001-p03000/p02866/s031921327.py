import sys
import math
MAX_INT = int(10e12)
MIN_INT = -MAX_INT
mod = 998244353
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
a = IL()
num = max(a)
aset = [0 for i in range(num+1)]

for i in a:
  aset[i] += 1
#print(aset)
if aset[0] == 1 and a[0] == 0:
  ans = 1
  for i in range(1,num+1):
    ans *= (aset[i-1]**aset[i]) %mod
    #print(aset[i-1], aset[i])
  print(ans %mod)

else:
  print(0)

"""
10
0 1 1 1 1 1 1 3 2 1
"""