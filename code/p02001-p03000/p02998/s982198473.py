def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    n = int(input())
    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    
    def unite(x,y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        else:
            if par[x] > par[y]:
                x,y = y,x
            par[x] += par[y]
            par[y] = x
            return True
    
    def size(x):
        return -par[find(x)]
    
    par = [-1]*(2*10**5+2)
    s = set()
    for _ in range(n):
        x, y = map(int, input().split())
        unite(x, 10**5+y)
        s.add(x)
    
    cnt = Counter()
    for x in s:
        cnt[find(x)] += 1

    res = 0
    for k, v in cnt.items():
        res += v * (size(k)-v)

    print(res-n)

if __name__ == '__main__':
    main()