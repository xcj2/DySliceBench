def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    from itertools import product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        b = a[0] // 2
        print((m-b)//(2*b) + 1)
        exit()
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
    b = lcm_group(a)
    for i in a:
        if (b//i) % 2 == 0:
            print(0)
            exit()

    print((m-b//2)//b + 1)

if __name__ == '__main__':
    main()
