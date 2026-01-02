N, X = map(int, input().split())


def f(n):
    # レベルnの総数
    if n == 0:
        return 1
    else:
        return 2 * f(n - 1) + 3


def g(n):
    # レベルnのpの数
    if n == 0:
        return 1
    else:
        return 2 * g(n - 1) + 1


def dfs(n, x):
    # 総数
    m = f(n)
    # 真ん中
    a = (m + 1) // 2

    if n == 0:
        return 1
    elif x == 1:
        return 0
    elif x < a:
        return dfs(n - 1, x - 1)
    elif x == a:
        return g(n - 1) + 1
    elif x >= a:
        return g(n - 1) + 1 + dfs(n - 1, x - a)
    elif x == m:
        return 2 * g(n - 1) + 1


ans = dfs(N, X)
print(ans)
