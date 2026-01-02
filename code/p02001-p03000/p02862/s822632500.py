import sys, math
mod = 10**9+7
X, Y = map(int, input().split())
if X>Y:
    X, Y = Y, X
if (X+Y)%3 !=0:
    print(0)
    sys.exit()
n = (X+Y)//3
d = (Y-X)
if n<d or (n-d)%2 != 0:
    print(0)
    sys.exit()
a = (n-d)//2
def make_fact(n):#0~nの階乗を求める
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1]*i%mod
    return fact
fact = make_fact(n)  
def make_fact_inv(n):#0~nの階乗のmodに関する逆元を求める
    fact_inv = [1]*(n+1)
    fact_inv[n] = pow(fact[n], mod-2, mod)#フェルマーの小定理
    for i in range(n, 0, -1):
        fact_inv[i-1] = fact_inv[i]*i%mod
    return fact_inv
fact_inv = make_fact_inv(n)

def comb(n, k):#nCk
    return fact[n]*fact_inv[k]*fact_inv[n-k]%mod

print(comb(n, a))