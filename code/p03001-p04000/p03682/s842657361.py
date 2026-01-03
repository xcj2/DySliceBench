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
    #mod = 1000000007

    N = int(input())
    xy = []
    for i in range(N):
        x,y = map(int, input().split())
        xy.append([x, y, i])
    x_sort = sorted(xy, key=lambda x: x[0])
    y_sort = sorted(xy, key=lambda x: x[1])

    #[cost, 頂点1, 頂点2]
    cost = []
    for i in range(N-1):
        cost.append([x_sort[i+1][0]-x_sort[i][0], x_sort[i][2], x_sort[i+1][2]])
        cost.append([y_sort[i+1][1]-y_sort[i][1], y_sort[i][2], y_sort[i+1][2]])
    cost = sorted(cost, key=lambda x: x[0])

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

    par = [-1]*N

    res = 0
    for c, v1, v2 in cost:
        if not same(v1, v2):
            unite(v1, v2)
            res += c
    print(res)


if __name__ == '__main__':
    main()