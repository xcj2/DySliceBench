import sys, os, math, bisect, itertools, collections, heapq, queue, copy, array

# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

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

parent = lambda i: math.floor(i / 2)
left = lambda i: 2 * i
right = lambda i: 2 * i + 1


def max_heapify(A, H, i):
    l = left(i) + 1
    r = right(i) + 1

    largest = i
    if l < H and A[l] > A[i]:
        largest = l
    if r < H and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, H, largest)


def build_max_heap(A, H):
    for i in reversed(range(H // 2)):
        max_heapify(A, H, i)


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    H = ii()
    heap = il()
    build_max_heap(heap, H)
    print('', *heap)


if __name__ == '__main__':
    main()

