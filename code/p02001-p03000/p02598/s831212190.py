#!/usr/bin/env python3
import collections as cl
import sys
import math


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


class Logs():
    def __init__(self, K, logs):
        self.K = K
        self.logs = logs

    def canCutUnderX(self, X):
        times = 0
        for log in self.logs:
            time = math.floor(log/X)
            if log % X == 0:
                time -= 1
            times += time
            if times > self.K:
                return False

        return True

    def solve(self):
        ans = self.nibutan(0, max(self.logs))
        return ans

    def nibutan(self, l, r):
        if l + 1 == r:
            return r
        c = (l + r) // 2

        if self.canCutUnderX(c):
            return self.nibutan(l, c)
        else:
            return self.nibutan(c, r)


def main():
    _, K = MI()
    logs = LI()

    solver = Logs(K, logs)
    print(solver.solve())


main()
