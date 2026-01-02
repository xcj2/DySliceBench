def binary_search_int(ok, ng, test, p):
    """
    :param ok: solve(x) = True を必ず満たす点
    :param ng: solve(x) = False を必ず満たす点
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if test(mid, p):
            ok = mid
        else:
            ng = mid
    return ok

def lcm(x,y):
    return x*y//gcd(x,y)

from math import gcd

A, B, C, D = map(int, input().split())
l = lcm(C,D)

def test1(x, p):
    return x*p<=B
b = [binary_search_int(0,10**18+1,test1, x) for x in [C, D, l]]

def test2(x, p):
    return x*p>=A

a = [binary_search_int(10**18+1, 0,test2, x) for x in [C, D, l]]

res = [x-y+1 if (x!=0 and y!=10**18+1) else 0 for x, y in zip(b, a)]


print((B-A+1)-res[0]-res[1]+res[2])