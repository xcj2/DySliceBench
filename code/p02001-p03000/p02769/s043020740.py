MAX = 10 ** 5 * 2
mod = 10 ** 9 + 7
frac = [1]
inv_frac=[1]
def pow(a, n):
    if n == 0 : return  1
    elif n == 1 : return a
    tmp = pow(a, n//2)
    tmp = (tmp * tmp) % mod
    if n % 2 == 1 :
        tmp = (tmp * a) % mod
    return tmp
def inv(x):
    return pow(x, mod - 2 )
for i in range(1,MAX + 1 ):
    frac.append( (frac[-1] * i) % mod )
    inv_frac.append(inv(frac[-1])%mod)
def comb(n, k):
    if k >= n or k < 0 : return 1
    return (frac[n]*inv_frac[n-k] * inv_frac[k]) %mod
n,k = map(int,input().split())
count=0
b=inv(n)
for i in range(min(n,k+1)):
    a=comb(n,i)
    count=(count+a*a*(n-i)*b)%mod
print(count)