import sys
import math
import numpy as np


def input():
    return sys.stdin.readline().rstrip()


def dist(y, z, d):
    ret = 0.0
    for i in range(d):
        ret += pow(y[i] - z[i], 2)
    return pow(ret, 0.5)


def main():
    n, d = [int(e) for e in input().split()]
    x = [[int(e) for e in input().split()] for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist_yz = dist(x[i], x[j], d)
            if math.ceil(dist_yz) == math.floor(dist_yz):
                ans += 1
    print(ans)


main()
