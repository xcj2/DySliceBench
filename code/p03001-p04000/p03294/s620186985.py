from functools import reduce
N = int(input())
a = list(map(int, input().split()))

def gcd_impl(n,m):
    for _ in range(10):
        t = n - m
        q = m > t
        if q:
            n = m
        else:
            n = t
        if q:
            m = t
        else:
            m = m
        if m == 0:
            return n
    return gcd_impl(m, n%m)

def gcd(n,m):
    if n > m:
        return gcd_impl(n,m)
    else:
        return gcd_impl(m,n)

def lcm(a,b):
    return (a*b)//gcd(a,b)

def lcm_list(lst):
    return reduce(lcm, lst)

M = lcm_list(a) - 1

res = 0
for i in a:
    res += M%i
print(res)