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
    #mod = 10**9 + 7

    N = int(input())
    n = int(N**0.5) + 1

    def check(i, N):
        while N%i==0:
            N //= i
            if N%i==1:
                return 1
        return 0

    def yakusuu(N):
        n = int(N**.5)+1
        res1 = []
        res2 = []
        for i in range(1, n):
            if N%i==0:
                res1.append(i)
                if N!=i**2:
                    res2.append(N//i)
        res2.reverse()
        return res1+res2
        
    res = 0

    for i in range(2, n):
        if (N%i)!=1:
            res += check(i, N)
    res += len(yakusuu(N-1))

    print(res)

if __name__ == '__main__':
    main()