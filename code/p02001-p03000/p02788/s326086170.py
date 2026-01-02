import sys
import bisect
import math
from operator import itemgetter
MAX_INT = int(10e12)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N, D, A = IL()
X = []
xx = []
H = []
for i in range(N):
  x, h = IL()
  xx.append(x)
  X.append([x, i])
  H.append(h)
else:
  xx.append(MAX_INT)
xx.sort()
X.sort(key=itemgetter(0))
data = [0]*(N+1)

D = D*2
damage = 0
ans = 0
for i in range(N):
  x,j = X[i]
  hp = H[j]
  damage += data[i]
  num = max(0,math.ceil((hp - damage)/A))
  damage += num*A
  ans += num
  rng = x + D
  nxt = bisect.bisect_right(xx, rng)
  data[nxt] -= num*A
#print(data)
#print(xx)
print(ans)

"""
9 2 1
1 5
2 4
3 3
4 2
5 1
6 2
7 3
8 4
9 5
"""