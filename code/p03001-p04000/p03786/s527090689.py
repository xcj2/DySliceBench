#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


class Solver():
    def __init__(self, target):
        self.target = target

    def bin_search(self, l, r):
        if l + 1 == r:
            if self.check(l):
                return l - 1
            return l

        c = (l+r) // 2

        is_c_achieve = self.check(c)

        if is_c_achieve:
            return self.bin_search(l, c)
        else:
            return self.bin_search(c, r)

    def check(self, c):
        others = cl.deque(self.target)
        others.remove(self.target[c])
        mine = self.target[c]

        while len(others) > 0:
            minest = others.popleft()
            if mine * 2 >= minest:
                mine += minest
            else:
                return False
        return True


def main():
    N = II()
    target = LI()
    target.sort()
    solver = Solver(target)
    ans = solver.bin_search(0, N - 1)
    print(N - ans - 1)


main()
