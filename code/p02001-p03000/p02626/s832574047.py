import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
A = LI()

a = A[0]
b = A[1]
c = 0
if len(A) >= 3:
    for i in range(2,N):
        c ^= A[i]

INF = 10**12

from functools import lru_cache

@lru_cache(maxsize=None)
def f(s,t,u):
    '''
    (s-x) ^ (t+x) == u たる x の最小値を返す
    '''
    if s == 0:
        if t == u:
            return 0
        else:
            return INF
    else:
        if (s & 1) ^ (t & 1) == u & 1:
            return min(2*f(s//2,t//2,u//2),2*f((s-1)//2,(t+1)//2,u//2)+1)  # 1の位が0か1か
        else:
            return INF

ans = f(a,b,c)
if ans >= a:
    print(-1)
else:
    print(ans)