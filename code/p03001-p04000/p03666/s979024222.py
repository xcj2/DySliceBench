import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]
def init_dp1(init, N): return [init for _ in range(N)]
def init_dp2(init, N, M): return [[init for _ in range(M)] for _ in range(N)]


def main():
    N, A, B, C, D = read_values()

    M = A + (N - 1) * D
    m = A + (N - 1) * C
    for _ in range(N):
        if m <= B <= M:
            print("YES")
            return
        
        M -= D + C
        m -= D + C

    print("NO")


if __name__ == "__main__":
    main()

