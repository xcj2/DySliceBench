import sys
import math
import bisect
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


# A
def A():
    s = input()
    if s == 'SUN':
        print(7)
    if s == "MON":
        print(6)
    if s == "TUE":
        print(5)
    if s == "WED":
        print(4)
    if s == "THU":
        print(3)
    if s == "FRI":
        print(2)
    if s == "SAT":
        print(1)
    return


# B
def B():
    al = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    n = I()
    s = S()
    for i in range(len(s)):
        ni = (al.index(s[i]) + n) % 26
        s[i] = al[ni]
    print(''.join(s))
    return


# C
def C():
    return


# D
def D():
    return


# E
def E():
    return


# F
def F():
    return


# Unittest
def resolve():
    B()
    return


# Solve
if __name__ == "__main__":
    B()
