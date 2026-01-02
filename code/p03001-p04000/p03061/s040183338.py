#どっちで出すか注意, rstrip注意
#提出前に見返すこと！
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

    N = int(input())
    A = list(map(int, input().split()))

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
    
    l = [0]
    for i in range(N-1):
        l.append(gcd(l[-1], A[i]))
    r = [0]
    for i in range(N-1, 0, -1):
        r.append(gcd(r[-1], A[i]))
    
    res = 0
    for i in range(N):
        res = max(res, gcd(l[i], r[-(i+1)]))
    print(res)


if __name__ == '__main__':
    main()
