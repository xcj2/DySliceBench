import math
from operator import mul
from functools import reduce
import sys

# sys.setrecursionlimit(int(2000000))
def main():
    X, Y = [int(n) for n in input().split()]
    if (2 * Y - X) % 3 != 0 or (2 * X - Y) % 3 != 0:
        print(0)
        return
    i = (2 * Y - X)//3
    j = (2 * X - Y)//3
    print(combinations_count(i+j, min(i,j),int(1e9+7)))

def combinations_count(n, k, M):
    if k == 0:
        return 1
    fn = 0
    fk = 0
    fnk = 0
    cur = 1
    M = int(1e9+7)
    for i in range(1, n+1):
        cur = (cur * i) % M
        if i == n:
            fn = cur
        if i == n-k:
            fnk = cur
        if i == k:
            fk = cur

    return (fn * (modpow(fk , (M-2), M)) * modpow(fnk , (M-2), M))%M
def modpow(a,b,M):
    if b == 1:
        return a % M
    if b % 2 == 1:
        return (modpow(a,(b-1)//2,M)**2 * a)%M
    return (modpow(a,b//2,M) ** 2) % M 
main()