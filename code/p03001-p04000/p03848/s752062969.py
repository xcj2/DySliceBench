#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    targets = LI()
    targets.sort()
    deque = cl.deque(targets)

    count = 1
    if N % 2 != 0:
        target = deque.popleft()
        if target != 0:
            print(0)
            return
        count = 2

    while len(deque) > 0:
        a = deque.popleft()
        b = deque.popleft()
        if a == b == count:
            count += 2
            continue
        else:
            print(0)
            return

    print(pow(2, (N//2), 10**9+7))


main()
