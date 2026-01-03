import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
T = LI()
A = LI()
mod = 10**9+7

minimum = [1]*N
maximum = [0]*N

for i in range(N):
    if i == 0:
        minimum[i] = T[i]
        maximum[i] = T[i]
    else:
        if T[i] != T[i-1]:
            minimum[i] = T[i]
            maximum[i] = T[i]
        else:
            maximum[i] = T[i]

for i in range(N-1,-1,-1):
    if i == N-1:
        minimum[i] = max(minimum[i],A[i])
        maximum[i] = min(maximum[i],A[i])
    else:
        if A[i] != A[i+1]:
            minimum[i] = max(minimum[i],A[i])
            maximum[i] = min(maximum[i],A[i])
        else:
            maximum[i] = min(maximum[i],A[i])

ans = 1
for i in range(N):
    if maximum[i] >= minimum[i]:
        ans *= maximum[i]-minimum[i]+1
        ans %= mod
    else:
        print(0)
        exit()
print(ans)
