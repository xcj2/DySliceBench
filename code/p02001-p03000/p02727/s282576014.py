import sys
import heapq
from operator import itemgetter
 
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

X,Y,A,B,C = IL()
p = IL()
q = IL()
r = IL()

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

d = []
heappop = heapq.heappop
heappush = heapq.heappush
for i in range(A):
  heappush(d, (-p[i],0))
for i in range(B):
  heappush(d, (-q[i],1))
for i in range(C):
  heappush(d, (-r[i],2))

acnt ,bcnt, ccnt = 0,0,0
cnt = 0
ans = 0
while acnt+bcnt+ccnt != X+Y:
  score,num = heappop(d)
  if num == 0:
    if acnt < X:
      acnt += 1
      ans -= score
  elif num == 1:
    if bcnt < Y:
      bcnt += 1
      ans -= score
  else:
    ccnt += 1
    ans -= score
print(ans)