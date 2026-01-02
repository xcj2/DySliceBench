def comb(n, r):
    if r<0 or r>n:
        return 0
    r=min(r, n-r)
    return g1[n]*g2[r]*g2[n-r]%MOD

MOD=10**9+7
MAXN=2000+10
g1=[1, 1]
g2=[1, 1]
inverse=[0, 1]

for i in range(2, MAXN+1):
    g1.append((g1[-1]*i)%MOD)
    inverse.append(-inverse[MOD%i]*(MOD//i)%MOD)
    g2.append((g2[-1]*inverse[-1])%MOD)

def f(n, k):
    if n<k:
        return 0
    if n==0 and k==0:
        return 1
    if k<1:
        return 0
    return f2(n-k, k)

def f2(n, k):
    return comb(n+k-1, k-1)

N, K=map(int, input().split())
for i in range(1, K+1):
    b=f(K, i)
    r=f(N-K, i-1)+2*f(N-K, i)+f(N-K, i+1)
    print((b*r)%MOD)