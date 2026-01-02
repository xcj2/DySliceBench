import sys
from collections import defaultdict
from queue import deque
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():

    n = gete(int)
    l = list(geta(int))
    l.sort()

    l_max = 2000
    # p[k]: number of sticks with length >= k
    p = [0] * (l_max + 1)

    cur = 0
    acc = n
    for i in range(l_max + 1):
        p[i] = acc

        if cur < n and i == l[cur]:
            while cur < n and l[cur] == i:
                acc -= 1
                cur += 1

    ans = 0
    for i, a in enumerate(l):
        for b in l[i + 1:]:
            ans += p[abs(a - b) + 1] - p[a + b]

            if abs(a - b) < a:
                ans -= 1

            if abs(a - b) < b:
                ans -= 1
    print(ans // 3)


if __name__ == "__main__":
    main()