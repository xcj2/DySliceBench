from functools import reduce
N = int(input())
a = list(map(int, input().split()))

def gcd_impl(n,m):
    K = 5
    for _ in range(80):
        t = n - m
        s = n - m*K
        q = t < m
        p = t < m*K
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
        if p:
            n = n
        else:
            n = s
    return gcd_impl(m, n%m)

def gcd_pre(n,m):
    for _ in range(4):
        t = n - m
        q = t < m
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
    return gcd_impl(n,m)

def gcd(n,m):
    if n > m:
        return gcd_pre(n,m)
    else:
        return gcd_pre(m,n)

def lcm(a,b):
    return (a*b)//gcd(a,b)

def lcm_list(lst):
    return reduce(lcm, lst)

M = lcm_list(a) - 1

res = 0
for i in a:
    res += M%i
print(res)