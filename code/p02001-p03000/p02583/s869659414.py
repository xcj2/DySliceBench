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
    L = read_list()
    res = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                T = [L[i], L[j], L[k]]
                if len(set(T)) == 3 and sum(T) > 2 * max(T):
                    res += 1
    print(res)



if __name__ == "__main__":
    main()

