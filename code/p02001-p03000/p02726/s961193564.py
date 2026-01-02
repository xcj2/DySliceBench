import sys
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def S(): return sys.stdin.readline()
def LS(): return sys.stdin.readline().split()
def LS2(N): return [sys.stdin.readline().split() for i in range(N)]
def FILL(i,h,w): return [[i for j in range(w)] for k in range(h)]
def sisha(num,digit): return Decimal(str(num)).quantize(Decimal(digit),rounding=ROUND_HALF_UP)
#'0.01'や'1E1'などで指定、整数に戻すならintをかます
MOD = 1000000007
INF = float("inf")
sys.setrecursionlimit(10**5+10)
#input = sys.stdin.readline
import sys
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def S(): return sys.stdin.readline()
def LS(): return sys.stdin.readline().split()
def LS2(N): return [sys.stdin.readline().split() for i in range(N)]
def FILL(i,h,w): return [[i for j in range(w)] for k in range(h)]
def sisha(num,digit): return Decimal(str(num)).quantize(Decimal(digit),rounding=ROUND_HALF_UP)
#'0.01'や'1E1'などで指定、整数に戻すならintをかます
MOD = 1000000007
INF = float("inf")
sys.setrecursionlimit(10**5+10)
#input = sys.stdin.readline

from collections import deque

N,X,Y=MI()
l = []
for i in range(N):
    if i!=0 and i!=N-1:
        n = [i-1,i+1]
    elif i==0:
        n = [1]
    else:
        n = [N-2]
    if i==X-1:
        n += [Y-1]
    if i==Y-1:
        n += [X-1]
    l.append(n)
ans = [0]*(N-1)
for i in range(N):
    dist = [-1]*N
    q=deque()
    q.append(i)
    dist[i]=0
    while q:
        u = q.popleft()
        for next in l[u]:
            if dist[next]==-1:
                dist[next]=dist[u]+1
                ans[dist[u]] += 1
                q.append(next)

[print(x//2) for x in ans]
