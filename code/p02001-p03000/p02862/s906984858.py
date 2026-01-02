'''
https://atcoder.jp/contests/abc145/tasks/abc145_d
'''
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    mod = 10**9 + 7

    X,Y = map(int, input().split())
    if (X+Y)%3 != 0:
        print(0)
        exit()

    a = (2*X-Y)//3
    b = (2*Y-X)//3

    if a<0 or b<0:
        print(0)
        exit()

    def extgcd(a, b):
        if b == 0:
            return a, 1, 0
        else:
            d, x, y = extgcd(b, a % b)
            x -= (a // b) * y
            return d, y, x
        
    def modinv(a, mod): 
        return extgcd(a, mod)[1] % mod

    def modcomb(n, k, mod):
        q, a = 1, 1
        for i in range(n-k+1, n+1):
            q = (q * i) % mod
        for i in range(2, k+1):
            a = (a * i) % mod
        return int(q * modinv(a, mod) % mod)

    print(modcomb(a+b, a, mod))

if __name__ == '__main__':
    main()