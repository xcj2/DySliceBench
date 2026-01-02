import bisect
import copy
import heapq
import sys
import itertools
import queue
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
    N, M, C = read_values()
    B = read_list()

    res = 0
    for _ in range(N):
        A = read_list()
        if sum(a * b for a, b in zip(A, B)) + C > 0:
            res += 1

    print(res)


if __name__ == "__main__":
    main()
