import bisect
import math
from collections import deque

def sRaw():
    return input().rstrip("\r")


def iRaw():
    return int(input())


def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))

INF = 1 << 29


def main():
    X,Y,A,B,C = isRaw()
    ps = isRaw()
    qs = isRaw()
    rs = isRaw()
    ps.sort(reverse=True)
    ps = ps[:X]
    qs.sort(reverse=True)
    qs = qs[:Y]
    rs.sort()
    pqr = ps+qs+rs
    pqr.sort(reverse=True)
    return sum(pqr[:X+Y])

if __name__ == "__main__":
    print(main())
