import sys
from copy import deepcopy
sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,x = MI()
A = LI()
B = deepcopy(A)
A += A

ans = sum(B)
for k in range(1,N+1):
    for i in range(N):
        B[i] = min(B[i],A[N+i-k])
    ans = min(ans,sum(B)+k*x)

print(ans)
