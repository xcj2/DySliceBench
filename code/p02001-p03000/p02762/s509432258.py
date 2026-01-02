import sys
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from collections import deque
from bisect import bisect_left
from itertools import product
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def LSI(): return list(map(int, list(sys.stdin.readline().rstrip())))

def LSI2(N): return [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(N)]
def S(): return sys.stdin.readline().rstrip()
def LS(): return sys.stdin.readline().split()
def LS2(N): return [sys.stdin.readline().split() for i in range(N)]
def FILL(i,h): return [i for j in range(h)]
def FILL2(i,h,w): return [FILL(i,w) for j in range(h)]
def FILL3(i,h,w,d): return [FILL2(i,w,d) for j in range(h)]
def FILL4(i,h,w,d,d2): return [FILL3(i,w,d,d2) for j in range(h)]
def sisha(num,digit): return Decimal(str(num)).quantize(Decimal(digit),rounding=ROUND_HALF_UP)
#'0.01'や'1E1''などで指定、整数に戻すならintをかます
MOD = 998244353
INF = float("inf")
sys.setrecursionlimit(10**6+10)
input = sys.stdin.readline

import sys
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from collections import deque
from bisect import bisect_left
from itertools import product
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def LSI(): return list(map(int, list(sys.stdin.readline().rstrip())))

def LSI2(N): return [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(N)]
def S(): return sys.stdin.readline().rstrip()
def LS(): return sys.stdin.readline().split()
def LS2(N): return [sys.stdin.readline().split() for i in range(N)]
def FILL(i,h): return [i for j in range(h)]
def FILL2(i,h,w): return [FILL(i,w) for j in range(h)]
def FILL3(i,h,w,d): return [FILL2(i,w,d) for j in range(h)]
def FILL4(i,h,w,d,d2): return [FILL3(i,w,d,d2) for j in range(h)]
def sisha(num,digit): return Decimal(str(num)).quantize(Decimal(digit),rounding=ROUND_HALF_UP)
#'0.01'や'1E1'などで指定、整数に戻すならintをかます
MOD = 998244353
INF = float("inf")
sys.setrecursionlimit(10**6+10)
input = sys.stdin.readline

N,M,K = MI()
F = [[] for _ in range(N+1)]
B = [[] for _ in range(N+1)]
for i in range(M):
    a,b = MI()
    F[a].append(b)
    F[b].append(a)
for i in range(K):
    c,d = MI()
    B[c].append(d)
    B[d].append(c)
D = {}
visited = [False for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

def dfs(i,root):
    if visited[i]:
        pass
    else:
        visited[i]=True
        parent[i] = root
        for next in F[i]:
            if visited[next]:
                continue
            D[root].add(next)
            dfs(next,root)


for root in range(1,N+1):
    if visited[root]:
        continue
    D[root]=set([root])
    dfs(root,root)
ans = [0]*N
for iam in range(1,N+1):
    temp_ans = len(D[parent[iam]])-len(F[iam])-1
    for block in B[iam]:
        if block in D[parent[iam]]:
            temp_ans -= 1
    ans[iam-1] = temp_ans

print(*ans)
