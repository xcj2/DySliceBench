import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
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

    def same(x, y):
        return find(x) == find(y)

    def size(x):
        return -par[find(x)]

    def members(x):
        root = find(x)
        return [i for i in range(n) if find(i) == root]

    def roots():
        return [i for i, x in enumerate(par) if x < 0]

    def group_count(self):
        return len(roots())

    n, m = map(int, input().split())
    par = [-1] * n
    m = map(int, read().split())
    ab = zip(m, m)
    abs = set()
    for a, b in ab:
        a -= 1
        b -= 1
        tmp = (min(a, b), max(a, b))
        abs.add(tmp)
    for abse in abs:
        unite(abse[0], abse[1])
    rs = roots()
    r = 0
    for rse in rs:
        r = max(r, size(rse))
    print(r)
if __name__ == '__main__':
    main()