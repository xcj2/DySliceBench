import bisect
from collections import deque
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# mod = 10 ** 9 + 7
mod = 998244353

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]



def main():
    N, X, M = read_values()
    F = [-1] * (M + 1)

    A = X
    t = 0
    while F[A] < 0:
        F[A] = t
        A = pow(A, 2, M)
        t += 1
    
    if t == 1:
        print(X * N)
        return
    d = (N - F[A]) // (t - F[A])
    r = ((N - F[A]) % (t - F[A])) + F[A]

    K = 0
    for _ in range(F[A], t):
        K += A
        A = pow(A, 2, M)
    
    K *= d

    A = X
    for _ in range(r):
        K += A
        A = pow(A, 2, M)

    print(K)


if __name__ == "__main__":
    main()

