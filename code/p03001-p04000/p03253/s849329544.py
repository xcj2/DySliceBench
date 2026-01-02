#http://nihaoshijie.hatenadiary.jp/entry/2018/02/03/115759
N,M=map(int,input().split())
P=10**9+7
def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)
def inv(x):
    return egcd(x,P)[0]
Z=2*10**5
Fact=[0 for i in range(Z+1)]
Finv=[0 for i in range(Z+1)]
Fact[0]=1
Finv[0]=1
for i in range(Z):
    Fact[i+1]=(Fact[i]*(i+1))%P
    Finv[i+1]=inv(Fact[i+1])%P
def C(n,k):
    return (Fact[n]*(Finv[k]*Finv[n-k])%P)%P
def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct
D=factorize(M)
ans=1
for seq in D:
    k=seq[1]
    ans=ans*C(k+N-1,N-1)
    ans=ans%P
print(ans)
