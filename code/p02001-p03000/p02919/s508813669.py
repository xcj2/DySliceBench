from sys import setrecursionlimit as SRL, stdin

SRL(10 ** 7)
rd = stdin.readline
rrd = lambda: map(int, rd().strip().split())

n = int(input())
p = list(rrd())

bit = [0] * 100005


def add(x):
    while x <= n:
        bit[x] += 1
        x += x & -x


def sum(x):
    tot = 0

    while x:
        tot += bit[x]
        x -= x & -x
    return tot


def search(x):
    tot = 0
    if x < 0:
        return tot
    for i in range(20)[::-1]:
        if (1 << i) + tot <= n and bit[(1 << i) + tot] <= x:
            tot += 1 << i
            x -= bit[tot]
    return tot + 1


idx = [0] * 100005

for i in range(n):
    idx[p[i]] = i + 1

ans = 0
for i in range(n, 0, -1):

    j = sum(idx[i])
    l1 = search(j - 1)
    l2 = search(j - 2)
    r1 = search(j)
    r2 = search(j + 1)

    tt = (idx[i] - l1) * (r2 - r1) + (r1 - idx[i]) * (l1 - l2)
    ans += tt * i
    add(idx[i])

print(ans)
