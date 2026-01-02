#create date: 2020-07-03 14:00

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    def unite(x, y):
        x = find(x); y = find(y)
        if x == y:
            return False
        else:
            if par[x] > par[y]:
                x, y = y, x
            par[x] += par[y]
            par[y] = x
            return True
    def same(x, y):
        return find(x) == find(y)
    def size(x):
        return -par[find(x)]


    n, m, k = na()
    par = [-1] * n
    friend = [0] * n
    block = [list() for i in range(n)]
    for i in range(m):
        a, b = na()
        a -= 1; b -= 1
        unite(a, b)
        friend[a] += 1
        friend[b] += 1
    for i in range(k):
        c, d = na()
        c -= 1; d -= 1
        block[c].append(d)
        block[d].append(c)
    #print(par, fb)
    for i in range(n):
        ans = size(i) - friend[i] - 1
        for b in block[i]:
            if same(i, b):
                ans -= 1
        print(ans, end=" ")
if __name__ == "__main__":
    main()