import math
import time
from collections import deque
from collections import defaultdict
from copy import deepcopy
import heapq

mod = 10 ** 9 + 7
t = time.time()



def iip():
    ret = [int(i) for i in input().split()]
    if len(ret) == 1:
        return ret[0]
    return ret


def conbination(n, r, mod):
    if n < r:
        return 0

    if r == 0 or n == 0:
        return 1

    ret = 1
    for i in range(n-r+1, n+1):
        ret *= i
        ret = ret % mod

    bunbo = 1
    for i in range(1, r+1):
        bunbo *= i
        bunbo = bunbo % mod

    ret = (ret * inv(bunbo, mod)) % mod
    #print(f"conbination {n}, {r} = {ret}")
    return ret

def inv(n, mod):
    return power(n, mod-2)

def power(n, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p//2) ** 2) % mod
    if p % 2 == 1:
        return (n * power(n, p-1)) % mod

def main():
    N, K = iip()

    for i in range(1, K+1):
        a = conbination(N-K+1, i, mod)
        b = conbination(K-1, i-1, mod)
        ans = (a*b) % mod
        #print(a)
        #print(b)
        print(ans)


main()