import sys
input = sys.stdin.readline
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

    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    pdic = {e :0 for e in range(n)}
    for i, pe in enumerate(p):
        pdic[pe] = i

    par = [-1] * n
    for _ in range(m):
        x, y = map(int, input().split())
        unite(x-1, y-1)

    r = 0
    for i1 in range(n):
        r += same(i1, pdic[i1+1])
    print(r)


if __name__ == '__main__':
    main()
