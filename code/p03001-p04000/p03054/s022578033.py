import functools
import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
import random
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


H, W, N = read_values()
YP, XP = read_index()
S = input().strip()
T = input().strip()


def main():
    X = [0, W]
    Y = [0, H]
    for t, s in zip(T[::-1], S[::-1]):
        if t == "L":
            X[1] = min(W, X[1] + 1)
        elif t == "R":
            X[0] = max(0, X[0] - 1)
        elif t == "U":
            Y[1] = min(H, Y[1] + 1)
        elif t == "D":
            Y[0] = max(0, Y[0] - 1)

        if s == "L":
            X[0] += 1
        elif s == "R":
            X[1] -= 1
        elif s == "U":
            Y[0] += 1
        elif s == "D":
            Y[1] -= 1

        if X[0] >= X[1] or Y[0] >= Y[1]:
            print("NO")
            return

    if X[0] <= XP < X[1] and Y[0] <= YP < Y[1]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

