from bisect import bisect_left, bisect_right
from collections import deque
from sys import stdin


def intersect(ss, i, j, mid, v):
    i = bisect_left(ss, ss[mid+1]-v, i, mid)
    ii = bisect_left(ss, ss[j]-v, i, mid) + 1
    j = bisect_right(ss, ss[mid]+v, mid, j+1) - 1
    jj = mid+1
    acc = 0
    sjj = ss[jj+1]
    for s in ss[i:ii]:
        if sjj <= s+v:
            jj = bisect_right(ss, s+v, jj, j+1) - 1
            sjj = ss[jj+1]
        acc += jj - mid

    acc += (jj - mid) * (mid - ii)
    return acc


def count(ss, s, t, v):
    q = deque()
    ret = 0
    q.append((s, t))

    while q:
        i, j = q.popleft()
        if ss[j] - ss[i] <= v:
            ret += (j-i) * (j-i+1) // 2
        elif j - i > 1:
            mid = (i + j) // 2
            q.append((i, mid))
            q.append((mid, j))
            ret += intersect(ss, i, j, mid, v)

    return ret


def run():
    n, q = [int(x) for x in input().split()]
    s = 0
    sums = [s]
    for v in map(int, stdin.readline().split()):
        s += v
        sums.append(s)

    qs = [int(x) for x in input().split()]
    sums.append(s + max(qs))

    for v in qs:
        print(count(sums, 0, n, v))


if __name__ == '__main__':
    run()


