def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math

    #inf = 10**17
    mod = 10**9 + 7

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
        # 素因数のリストを返す(0, 1は空)

    # aの逆元を求める
    def inv(a, mod=mod):
        return pow(a, mod-2, mod)

    n = int(input())
    a = list(map(int, input().split()))


    lcm = [0]*(max(a)+1)
    for i in a:
        l = prime_decomp(i)
        c = Counter(l)
        for k, v in c.items():
            if lcm[k] < v:
                lcm[k] = v
    
    b = 1
    for i in range(len(lcm)):
        if lcm[i] != 0:
            b *= pow(i, lcm[i], mod)
    
    if n == 1:
        print(1)
    else:
        res = 0
        for i in a:
            res += inv(i)
        print(res*b%mod)

if __name__ == '__main__':
    main()