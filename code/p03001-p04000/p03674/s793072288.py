from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
mod = 10**9 + 7

def comb(n,k,p):
    """power_funcを用いて(nCk) mod p を求める"""
    from math import factorial
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1
    a=factorial(n) %p
    b=factorial(k) %p
    c=factorial(n-k) %p
    return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p
def power_func(a,b,p):
    """a^b mod p を求める"""
    if b==0: return 1
    if b%2==0:
        d=power_func(a,b//2,p)
        return d*d %p
    if b%2==1:
        return (a*power_func(a,b-1,p ))%p
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m


for key, val in cnt.items():
    if val == 2:
        doubled_num = key
        break

left = None
for i, a in enumerate(A):
    if a == doubled_num:
        if left == None:
            left = i
        else:
            right = i

rest = n - right
base_numerator = n+1
base_denominator = 1
base = (base_numerator * mod_inv(base_denominator, mod)) % mod
duplicate_numerator = left + rest + 1
duplicate_denominator = 0
duplicate = 1
for i in range(n+1):
    #print("base", base_numerator, base_denominator)
    #print("dup", duplicate_numerator, duplicate_denominator)
    #print(base, duplicate)
    print((base - duplicate) % mod)

    base_numerator -= 1
    base_denominator += 1
    base *= base_numerator * mod_inv(base_denominator, mod)
    base %= mod
    duplicate_numerator -= 1
    duplicate_denominator += 1
    duplicate *= duplicate_numerator * mod_inv(duplicate_denominator, mod)
    duplicate %= mod