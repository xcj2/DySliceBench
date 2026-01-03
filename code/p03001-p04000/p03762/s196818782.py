import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,M = MI()
X = LI()
Y = LI()
mod = 10**9+7

r = sum((i*(N-i)*(X[i]-X[i-1])) % mod for i in range(1,N))
r %= mod

ans = 0
for i in range(1,M):
    ans += r*i*(M-i)*(Y[i]-Y[i-1]) % mod
    ans %= mod

print(ans)
