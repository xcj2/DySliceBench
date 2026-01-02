#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()

    que = cl.deque(list(range(1, 10)))

    while N > 1:
        target = que.popleft()
        if target % 10 != 0:
            que.append(target*10 + (target % 10) - 1)

        que.append(target*10 + (target % 10))

        if target % 10 != 9:
            que.append(target*10 + (target % 10) + 1)
        N -= 1

    ans = que.popleft()

    print(ans)


main()
