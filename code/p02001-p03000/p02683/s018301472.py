import sys
from math import log2,floor,ceil,sqrt
# import bisect
sys.setrecursionlimit(10**5)
# from collections import deque

Ri = lambda : [int(x) for x in sys.stdin.readline().split()]
ri = lambda : sys.stdin.readline().strip()
 
def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
INF = 10 ** 18
MOD = 10**9+7

def backtrack(arr,cur,ans):
    if cur == n:
        alg = [0]*m
        cost  = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                cost+=c[i]
                for j in range(m):
                    alg[j] += lis[i][j]
        flag = True
        for i in range(m):
            if alg[i] < k:
                flag = False
                break
        if flag :
            ans[0] = min(ans[0],cost)
        return
    arr[cur] = 0
    backtrack(arr,cur+1,ans)
    arr[cur] = 1
    backtrack(arr,cur+1,ans)
    arr[cur] = 0

n,m,k  = Ri()
c = [0]*n
lis = []
for i in range(n):
    temp = Ri()
    c[i] = temp[0]
    lis.append(temp[1:])

arr = [0]*n
ans = [INF]
backtrack(arr,0,ans)
if ans[0] == INF:
    print(-1)
else:
    print(ans[0])