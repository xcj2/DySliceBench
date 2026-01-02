import sys, os, math, bisect, itertools, collections, heapq, queue
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from decimal import Decimal
from collections import defaultdict, deque
import copy

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def bubble_sort(A, N):
    for i in range(N):
        for j in reversed(range(i + 1, N)):
            if A[j][1:] < A[j - 1][1:]:
                A[j], A[j - 1] = A[j - 1], A[j]


def selection_sort(A, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j][1:] < A[minj][1:]:
                minj = j
        if minj != i:
            A[i], A[minj] = A[minj], A[i]


def is_stable(bubble, selection):
    for b, s in zip(bubble, selection):
        if b != s:
            return False
    else:
        return True


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    A = sl()
    bubble_list = copy.copy(A)
    selection_list = copy.copy(A)

    bubble_sort(bubble_list, N)
    selection_sort(selection_list, N)
    print(*bubble_list)
    print('Stable')
    print(*selection_list)
    print('Stable' if is_stable(bubble_list, selection_list) else 'Not stable')


if __name__ == '__main__':
    main()

