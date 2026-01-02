import sys


def root(x):
    if parent[x] < 0:
        return x
    else:
        parent[x] = root(parent[x])
        return parent[x]


def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return False
    else:
        if y > x:
            x, y = y, x
        parent[x] += parent[y]
        parent[y] = x
        return True


def size(node):
    return -parent[root(node)]

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    input_list = [list(map(int, input().split())) for _ in range(m)]
    parent = [-1] * n
    ans_list = []
    ans = int(n*(n-1)/2)
    for a, b in input_list[::-1]:
        ans_list.append(ans)
        tmp = size(a-1) * size(b-1)
        if unite(a-1, b-1):
            ans -= tmp

    for ans in ans_list[::-1]:
        print(ans)
