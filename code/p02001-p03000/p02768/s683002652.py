import sys
from pprint import pprint

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

  
def mod_inv(a,m):
    if a == 0:
        return 0
    x = extgcd(a,m)[0]
    return (m+x%m)%m


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

if __name__ == '__main__':
    mod = 10**9 + 7
    n, a, b = map(int, sys.stdin.readline().strip().split(" "))
    # print(n, a, b, mod)

    denominator = 1
    numerator = 1
    for i in range(1, a+1):
        # print(n-i+1, i)
        numerator *= (n-i+1)
        numerator %= mod
        denominator *= i
        denominator %= mod
    # print(numerator, denominator)
    cmb_a = numerator * mod_inv(denominator, mod)
        
    denominator = 1
    numerator = 1
    for i in range(1, b+1):
        # print(n-i+1, i)
        numerator *= (n-i+1)
        numerator %= mod
        denominator *= i
        denominator %= mod
    # print(numerator, denominator)
    cmb_b = numerator * mod_inv(denominator, mod)
        
    # print(pow(2, n, mod) - 1, cmb_a, cmb_b)
    ans = pow(2, n, mod) - 1 - cmb_a - cmb_b
    print(ans % mod)