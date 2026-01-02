import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
from functools import lru_cache
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
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
    N, M, K = read_values()
    A = read_list()
    B = read_list()

    if sum(A) + sum(B) <= K:
        print(N + M)
        return

    SB = [0] * (M + 1)
    for i in range(M):
        SB[i + 1] = SB[i] + B[i]

    res = V(max, 0)
    for i in range(N):
        j = bisect.bisect_right(SB, K) - 1
        res.ud(j + i)
        K -= A[i]
        if K < 0:
            break
    else:
        j = bisect.bisect_right(SB, K) - 1
        res.ud(j + N)
    
    print(res)


if __name__ == "__main__":
    main()

