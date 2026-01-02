'''
https://atcoder.jp/contests/abc150/tasks/abc150_d
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
    #mod = 10**9 + 7

    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a = list(set(a))

    if len(a) == 1:
        if m >= a[0]//2:
            print((m-a[0]//2) // a[0] + 1)
        else:
            print(0)
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
    g = gcd_group(a)
    for i in a:
        if (i//g)%2 == 0:
            print(0)
            exit()
    lcm = lcm_group(a)
    semi_lcm = lcm // 2
    if m >= semi_lcm:
        print((m-semi_lcm)//lcm + 1)
    else:
        print(0)


if __name__ == '__main__':
    main()