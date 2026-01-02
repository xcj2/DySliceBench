def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    mod = 10**9 + 7

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

    n,k = map(int, input().split())
    #k個ある青のボールをi個に分ける
    for i in range(1, k+1):
        if i > n-k+1:
            print(0)
        else:
            print((modcomb(k-1, k-i, mod) * modcomb(n-k+1, i, mod))% mod)
        
if __name__ == '__main__':
    main()