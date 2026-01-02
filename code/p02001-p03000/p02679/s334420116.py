import sys
from collections import defaultdict
dic1 = defaultdict(int)
dic2 = defaultdict(int)
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
mod = 10**9+7
def pow(n,p,mod=10**9+7): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a//gcd(a,b)*b)
def to_standard_form(a, b):
    if a == 0:
        return (0, 1)
    g = gcd(a, b)
    a //= g
    b //= g
    if a < 0:
        return (-a, -b)
    return (a, b)
n = int(readline())
zero = 0
for i in range(n):
    a,b= map(int,readline().split())
    if a == b == 0:
        zero += 1
        continue
    plamai = 1 if a*b > 0 else 0
    a,b = to_standard_form(a,b)
    if b <= 0:
        dic2[(a,b)] += 1
    else:
        dic1[(b,-a)] += 1
        dic2[(b,-a)] += 0

ans = zero
k = 1
for key,cnt in dic2.items():
    cnt2 = dic1[key]
    x = pow(2,cnt)+pow(2,cnt2)
    k = k*(x-1)%mod
print((ans+k-1)%mod)