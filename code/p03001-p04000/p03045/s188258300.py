from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)

from collections import Counter

def main():
    n, m = map(int, input().split())
    par = [i for i in range(n)]
    size = [1] * n

    def root(x):
        if par[x] == x:
            return x
        else:
            par[x] = root(par[x])
            return par[x]

    def same(x, y):
        return root(x) == root(y)

    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return
        par[x] = y
        size[y] += size[x]
    
    for _ in range(m):
        x, y, z = map(int, input().split())
        unite(x - 1, y - 1)
    for i in range(n):
        root(i)
    print(len(Counter(par)))

main()