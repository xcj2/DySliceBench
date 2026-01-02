def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

import sys
sys.setrecursionlimit(4100000)
rl = sys.stdin.readline

N,M,K  =Ints()

mod = 998244353


#N = # Combination　における，最大整数部分
#mod = # 大体modで割った余りを求めさせられる．

def make_bikkuri(N):
    bikkuri = [1]
    for i in range(1,N+1):
        bikkuri.append((bikkuri[-1]*i)%mod)
    return bikkuri

bikkuri = make_bikkuri(N)

def nCk(n,k):
    ans = bikkuri[n] * pow(bikkuri[k], mod-2, mod) * pow(bikkuri[n-k], mod-2, mod)
    return ans%mod


ans = 0

for i in range(K+1):
    ans += nCk(N-1,i)*pow(M-1,N-1-i,mod)
    ans %= mod
ans *= M
ans %= mod

print(ans)
#print(pow(100-1,))