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

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    def gcd_group(arr):
        g = gcd(arr[0], arr[1])
        for i in range(2, len(arr)):
            g = gcd(g, arr[i])
        return g
    
    def lcm(a, b):
        g = gcd(a, b)
        return (a*b)//g
    
    def lcm_group(arr):
        l = lcm(arr[0], arr[1])
        for i in range(2, len(arr)):
            l = lcm(l, arr[i])
        return l
    
    # groupは要素1つでエラー

    # aの逆元を求める
    def inv(a, mod=mod):
        return pow(a, mod-2, mod)

    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(1)
    else:
        l = lcm_group(a)
        res = 0
        for i in a:
            res += inv(i)
        print(res*l%mod)

if __name__ == '__main__':
    main()