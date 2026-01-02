import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(100000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


class V:
    def __init__(self, f, v=None):
        self.f = f
        self.v = v
 
    def __str__(self):
        return str(self.v)
 
    def ud(self, n):
        if n is None:
            return

        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n) 


def main():
    N = int(input())
    A = read_list()
    dp = [[-10 ** 20 for _ in range(2)] for _ in range(N // 2 + 5)] 

    dp[0][0] = 0
    dp[1][1] = A[0]
    for i in range(1, N):
        for k in range(i // 2 + 2, max(0, i // 2 - 2), -1):
            dp[k][0] = max(dp[k][1], dp[k][0])
            dp[k][1] = dp[k - 1][0] + A[i]

    print(max(dp[N // 2]))


if __name__ == "__main__":
    main()
