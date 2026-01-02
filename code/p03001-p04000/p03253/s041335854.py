def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    mod = 10**9 + 7

    n,m = map(int, input().split())
    # 素因数分解
    def prime_decomp(n):
        i = 2
        res = []
        while i ** 2 <= n:
            while n % i==0:
                n //= i
                res.append(i)
            i += 1
        if n > 1:
            res.append(n)
        return res
    a = prime_decomp(m)
    c = Counter(a)

    def ncr(n, r, mod):
        r = min(r, n-r)
        numer = denom = 1
        for i in range(1, r+1):
            numer = numer * (n+1-i) % mod
            denom = denom * i % mod
        return numer * pow(denom, mod-2, mod) % mod

    res = 1
    for v in c.values():
        res *= ncr(n-1+v, n-1, mod)
    print(res % mod)

if __name__ == '__main__':
    main()