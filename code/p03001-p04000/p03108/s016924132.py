N, M = map(int, input().split())

# 最初は全て繋がっているが、1本ずつ崩落していく。
# uniteし続けて、最終的に親が違うものは分離しているとみなせる？


parents = None


def root(x):
    if parents[x] < 0:
        return x
    if parents[x] == x:
        return x
    parents[x] = root(parents[x])
    return parents[x]


count = 0


def unit(x, y):
    root_x = root(x)
    root_y = root(y)
    if root_x == root_y:
        return

    if parents[root_x] > parents[root_y]:
        root_x, root_y = root_y, root_x
    parents[root_x] += parents[root_y]
    parents[root_y] = root_x


def same(x, y):
    root_x = root(x)
    root_y = root(y)
    return (root_x == root_y)


def size(x):
    return -parents[root(x)]


es = []
for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    es.append((a, b))


parents = [-1] * N
ans = [0 for _ in range(M + 1)]
ans[M] = N * (N - 1) // 2
for i, e in enumerate(es[::-1]):
    # print('===========')
    a, b = e
    if root(a) != root(b):
        # print(size(a), size(b))
        x, y = size(a), size(b)
    else:
        x, y = 0, 0
    unit(a, b)
    ans[M - 1 - i] = ans[M - i] - (x * y)
    # print(parents)


# print(ans)
for num in ans[1:]:
    print(num)
