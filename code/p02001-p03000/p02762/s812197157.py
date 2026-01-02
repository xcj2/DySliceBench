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

    n,m,k = map(int, input().split())
    
    def find(par, x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par, par[x])
            return par[x]
    
    def unite(par, x,y):
        x = find(par,x)
        y = find(par,y)
        if x == y:
            return False
        else:
            if par[x] > par[y]:
                x,y = y,x
            par[x] += par[y]
            par[y] = x
            return True
    
    def same(par, x,y):
        return find(par, x) == find(par, y)
    
    def size(par, x):
        return -par[find(par, x)]

    def members(par, x, n):
        root = find(par, x)
        return [i for i in range(n) if find(par, i) == root]
    
    friend = [-1]*n
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
        unite(friend, a-1, b-1)

    block = [[] for _ in range(n)] #頂点数, 場合によって変える
    for _ in range(k):
        a,b = map(int, input().split())
        block[a-1].append(b-1)
        block[b-1].append(a-1)

    res = []
    for i in range(n):
        p = size(friend, i) - 1 -len(adj[i])
        for q in block[i]:
            if same(friend, i, q):
                p -= 1
        res.append(p)
    print(*res)

if __name__ == '__main__':
    main()