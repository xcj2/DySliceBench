# https://onlinejudge.u-aizu.ac.jp/problems/DSL_1_A

n, q = list(map(int, input().split()))
parents = [-1 for _ in range(n)]


def root(i):
    if parents[i] == -1:
        return i
    else:
        parents[i] = root(parents[i])
        return parents[i]


def unite(x, y):
    if same(x, y):
        return

    x = root(x)
    y = root(y)
    parents[y] = x


def same(x, y):
    return root(x) == root(y)


for _ in range(q):
    com, x, y = list(map(int, input().split()))
    if com == 0:
        unite(x, y)
    elif com == 1:
        if same(x, y):
            print(1)
        else:
            print(0)
    else:
        raise Exception

