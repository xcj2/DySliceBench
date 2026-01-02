# ABC075c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]


def root(x):
    if(tree[x] == x):
        return x
    tree[x] = root(tree[x])
    return tree[x]  # 経路圧縮


def same(x, y):  # xとyが同じ木に属するか
    return root(x) == root(y)


def unite(x, y):
    x = root(x)
    y = root(y)
    if(x == y):
        return
    tree[x] = y


ans = 0
for i in range(m):
    # print('init')
    tree = []
    for k in range(n+1):
        tree.append(k)
    for j in range(m):
        if (i == j):
            continue
        # print(a[j])
        unite(a[j][0], a[j][1])
    flag = True
    for j in range(1, n+1):
        for k in range(j + 1, n+1):
            if (not same(j, k)):
                flag = False
    if (not flag):
        ans += 1
print(ans)