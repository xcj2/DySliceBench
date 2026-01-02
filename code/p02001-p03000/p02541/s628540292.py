n=int(input())
def fct(x):
    res=[]
    sq=int(x**(1/2))+7
    if x%2==0:
        cnt=1
        while x%2==0:
            cnt*=2
            x//=2
        res.append(cnt)
    for i in range(3,sq,2):
        if x%i==0:
            cnt=1
            while x%i==0:
                cnt*=i
                x//=i
            res.append(cnt)
    if x>1:
        res.append(x)
    res=list(set(res))
    return res


#https://tex2e.github.io/blog/crypto/crt
from functools import reduce
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def chinese_remainder(a, n):
    # a := [a1, a2, ..., ak]
    # n := [n1, n2, ..., nk]
    total = 0
    prod = reduce(lambda x, y: x*y, n)
    for n_i, a_i in zip(n, a):
        b_i = prod // n_i
        total += a_i * b_i * modinv(b_i, n_i)
    return total % prod

p=fct(2*n)
l=len(p)
bit=1<<l
k=10**20
for i in range(bit):
    f1=1;f2=1
    for j in range(l):
        if (i>>j)&1:
            f1*=p[j]
        else:
            f2*=p[j]
    tmp=chinese_remainder([0,-1],[f1,f2])
    if tmp:
        k=min(k,tmp)
print(k)
