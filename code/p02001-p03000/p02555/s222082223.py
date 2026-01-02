import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


S = I()
mod = 10**9+7

kaijou = [1]
for i in range(1,S):
    kaijou.append((kaijou[-1]*i) % mod)

inv = [1]
for i in range(1,S):
    inv.append(pow(kaijou[i],mod-2,mod))


def nCr(n,r):
    if n < r:
        return 0
    return (kaijou[n]*inv[r]*inv[n-r]) % mod


ans = 0
for i in range(1,S//3+1):
    if S-3*i >= 0:
        ans += nCr(S-1-2*i,i-1)
        ans %= mod

print(ans)
