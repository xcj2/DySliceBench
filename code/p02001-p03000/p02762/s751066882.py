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

    n, m, k = map(int, input().split())
    num_of_friends = [-1] * n
    par = [-1] * n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        unite(a, b)
        num_of_friends[a] += -1
        num_of_friends[b] += -1
    roots = defaultdict(int)
    #roots = {e: set() for e in range(n)}
    for i2 in range(n):
        roots[find(i2)] += 1
    for i3 in range(n):
        #num_of_friends[i3] += len(roots[find(i3)])
        num_of_friends[i3] += roots[find(i3)]
    for _ in range(k):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if find(c) == find(d):
            num_of_friends[c] -= 1
            num_of_friends[d] -= 1

    for i in range(n):
        print(num_of_friends[i], end=' ')

if __name__ == '__main__':
    main()