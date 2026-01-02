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
    #mod = 10**9 + 7

    a,b,c,d = map(int, input().split())
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
    a -= 1
    x = a - a//c - 1 - a//d - 1 + a//lcm(c, d) + 1
    y = b - b//c - 1 - b//d - 1 + b//lcm(c, d) + 1
    print(y-x)

if __name__ == '__main__':
    main()