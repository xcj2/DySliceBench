import sys
from collections import deque
import heapq
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N,M = IL()
ab = [IL() for i in range(N)]
data = [[] for i in range(M+1)]
able = []

hpop = heapq.heappop
hpush = heapq.heappush

for d,v in ab:
  if d > M:
    continue
  else:
    data[d].append(-v)

ans = 0
for i in range(1,M+1):
  if data[i] == 0:
    continue
  else:
    #print(data[i])
    for l in data[i]:
      hpush(able,l)
  #print(able)
  if able:
    ans -= hpop(able)
    #print(ans)

print(ans)