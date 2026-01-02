import itertools

H, W, K = map(int, input().split())
A = [input() for _ in range(H)]

ans = 0
cnt = 0

for a in A:
    for i in range(W):
        if a[i] == "#":
            cnt += 1


def countData(lhs, rhs):
    cnt = 0
    for i in range(H):
        if i in lhs:
            continue
        for j in range(W):
            if j in rhs:
                continue
            if A[i][j] == '#':
                cnt += 1
    return cnt


def countRow(lhs, rhs):
    cnt = 0
    for i in range(H):
        if i == lhs:
            continue
        if i == rhs:
            continue
        for j in range(W):
            if A[i][j] == '#':
                cnt += 1
    return cnt


def countCol(lhs, rhs):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if j == lhs:
                continue
            if j == rhs:
                continue
            if A[i][j] == '#':
                cnt += 1
    return cnt


if cnt < K:
    print(0)
    exit()

stRowlist = [i for i in range(H)]
stCollist = [i for i in range(W)]

# 行列
for i in range(H):
    for rows in itertools.combinations(stRowlist, i):
        for j in range(W):
            for cols in itertools.combinations(stCollist, j):
                cnt = countData(rows, cols)
                if (cnt == K):
                    ans += 1


print(ans)
