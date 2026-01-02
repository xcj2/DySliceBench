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
    tasks = []

    for i in range(N):
        task = LI()
        tasks.append([task[1], task[0]])
    tasks.sort()

    sum_time = 0

    for task in tasks:
        sum_time += task[1]
        if sum_time > task[0]:
            print("No")
            return

    print("Yes")


main()
