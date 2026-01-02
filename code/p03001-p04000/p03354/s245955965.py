def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n,m = map(int, input().split())
    p = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(m)]

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
    
    def same(x,y):
        return find(x) == find(y)
    
    par = [-1]*n

    for x, y in xy:
        if same(x-1, y-1) == False:
            unite(x-1, y-1)
    res = 0
    for i in range(n):
        if i == p[i]-1:
            res += 1
        else:
            if same(i, p[i]-1):
                res += 1
    print(res)

if __name__ == '__main__':
    main()