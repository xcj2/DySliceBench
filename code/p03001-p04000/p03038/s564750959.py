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
    n, m = MI()
    a = LI()

    a.sort()

    counter = cl.Counter({})

    for i in range(m):
        b, c = MI()
        counter.update({c: b})
    items = counter.items()
    items = sorted(items, key=lambda x: x[0], reverse=True)
    values, counts = map(list, zip(*items))

    lergest = 0
    finish = False
    for i in range(n):

        while not finish and a[i] > values[lergest]:
            lergest += 1
            if lergest == len(values):
                finish = True
                break
        if finish:
            break
        a[i] = values[lergest]
        counts[lergest] -= 1
        if counts[lergest] == 0:
            lergest += 1
            if lergest == len(values):
                break
    print(sum(a))


main()
