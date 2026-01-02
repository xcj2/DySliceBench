import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N = int(input())
    S = [input().strip() for _ in range(N)]
    print(sum(N if all(S[(i - a) % N][j] == S[(j - a) % N][i] for i in range(N) for j in range(N)) else 0 for a in range(N)))


if __name__ == "__main__":
    main()
