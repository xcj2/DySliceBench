import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 998244353

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N = int(input())
    A = read_lists(N)
    
    res = 0
    for i in range(N):
        for j in range(i + 1, N):
            if i == j:
                continue

            for k in range(N):
                if k in (i, j):
                    continue

                if A[i][j] == A[i][k] + A[k][j]:
                    break

                if A[i][j] > A[i][k] + A[k][j]:
                    print(-1)
                    return
            else:
                res += A[i][j]
    
    print(res)


if __name__ == "__main__":
    main()

