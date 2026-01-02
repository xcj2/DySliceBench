import sys

input = sys.stdin.buffer.readline
n, q = map(int, input().split())
C = list(map(int, input().split()))
LR = []
for i in range(q):
    l, r = map(int, input().split())
    LR.append((l, r, i))
LR.sort(key=lambda x: x[1])


BIT = [0] * (n + 1)


def update(idx, val):
    while idx <= n:
        BIT[idx] += val
        idx += idx & (-idx)


def query(idx):
    res = 0
    while idx > 0:
        res += BIT[idx]
        idx -= idx & (-idx)
    return res


pos = [-1] * (n + 1)


def func(idx):
    temp = C[idx]
    if pos[temp] == -1:
        pos[temp] = idx + 1
        update(idx + 1, 1)
    else:
        pre = pos[temp]
        pos[temp] = idx + 1
        update(pre, -1)
        update(idx + 1, 1)


ans = [0] * (q)
idx = 0
for i in range(q):
    l, r, ans_num = LR[i]
    # l,rは0-indexに戻す
    l -= 1
    r -= 1
    while idx < r + 1:  # rになるまで増やす
        if idx < n:  # n超えないように注意
            func(idx)
            idx += 1
        else:
            break
    res = 0
    res += query(r + 1)
    if l > 0:
        res -= query(l)
    ans[ans_num] = res

print(*ans, sep="\n")
