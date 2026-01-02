'''
https://atcoder.jp/contests/abc120/tasks/abc120_d
'''
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations
    #from itertools import accumulate, product
    from bisect import bisect_left,bisect_right
    from math import floor, ceil
    #from operator import itemgetter

    #mod = 1000000007

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
    
    def size(x):
        return -par[find(x)]
    
    #xが属するグループの要素全てを返す
    def members(x, n):
        root = find(x)
        return [i for i in range(n) if find(i) == root]
    
    #全ての根の要素を返す
    def roots():
        return [i for i, x in enumerate(par) if x < 0]

    n,m = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(m)]
    par = [-1]*n
    res = []
    total = n*(n-1)//2
    for a,b in edge[::-1]:
        a -= 1
        b -= 1
        res.append(total)
        if same(a,b):
            continue
        else:
            total -= size(a)*size(b)
            unite(a,b)

    for i in res[::-1]:
        print(i)

if __name__ == '__main__':
    main()