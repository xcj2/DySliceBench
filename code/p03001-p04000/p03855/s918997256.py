import sys
input = sys.stdin.buffer.readline
from collections import defaultdict
def main():
    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        else:
            if par[x] > par[y]:
                x, y = y, x
            par[x] += par[y]
            par[y] = x
            return True
    def members(x):
        root = find(x)
        return [i for i in range(n) if find(i) == root]

    def find2(x):
        if par2[x] < 0:
            return x
        else:
            par2[x] = find2(par2[x])
            return par2[x]
    def unite2(x, y):
        x = find2(x)
        y = find2(y)
        if x == y:
            return False
        else:
            if par2[x] > par2[y]:
                x, y = y, x
            par2[x] += par2[y]
            par2[y] = x
            return True
    def members2(x):
        root2 = find2(x)
        return [i for i in range(n) if find2(i) == root2]

    n, k, l = map(int, input().split())
    par = [-1] * n
    par2 = [-1] * n
    for _ in range(k):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        unite(a, b)
    for _ in range(l):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        unite2(c, d)

    root_pairs = defaultdict(int)
    for i in range(n):
        root_pairs[find(i), find2(i)] += 1

    for i in range(n):
        print(root_pairs[find(i), find2(i)], end=' ')

if __name__ == '__main__':
    main()