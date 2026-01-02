import math
import time
from collections import deque
from collections import defaultdict
from copy import deepcopy

mod = 10 ** 9 + 7
t = time.time()


def inv(n, mod):
    return power(n, mod-2)

def iip():
    ret = [int(i) for i in input().split()]
    if len(ret) == 1:
        return ret[0]
    return ret

def power(n, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return ((power(n, p//2) % mod) ** 2) % mod
    if p % 2 == 1:
        return (n * power(n, p-1)) % mod

def main():
    X, Y = iip()
    aa = (int(-X) + int(2*Y)) // 3
    bb = (int(-Y) + int(2*X)) // 3
    if (int(-X) + int(2*Y)) % 3 != 0 or  (int(-Y) + int(2*X)) % 3 != 0:
        print(0)
        exit()

    if X > 2*Y or Y > 2*X:
        print(0)
        exit()

    a = min(aa, bb)
    b = max(aa, bb)

    npr = 1
    bunbo = 1
    for i in range(1, a+1):
        npr *= (i+b)
        npr = npr % mod

        bunbo *= i
        bunbo = bunbo % mod

    ans = npr * inv(bunbo, mod) % mod

    print(ans)



main()