n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))


def memoize(f):  # メモ化関数
    table = [{} for _ in range(n+1)]

    def func(cur, m):
        if m not in table[cur]:
            table[cur][m] = f(cur, m)
        return table[cur][m]
    return func


# メモ再帰で書く
@memoize
def dfs(cur, m):
    if m == 0:
        return True
    if cur >= n:
        return False
    res = dfs(cur+1, m) | dfs(cur+1, m-A[cur])
    return res


for num in m:
    if dfs(0, num):
        print('yes')
    else:
        print('no')

