import sys, os, math, bisect, itertools, collections, heapq, queue

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


def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L, R = [0] * (n1 + 1), [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]

    L[n1] = float('INF')
    R[n2] = float('INF')

    i, j = 0, 0
    compare_cnt = 0
    for k in range(left, right):
        compare_cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return compare_cnt


def merge_sort(A, left, right):
    cnt = 0
    if left + 1 < right:
        mid = (left + right) // 2
        cnt += merge_sort(A, left, mid)
        cnt += merge_sort(A, mid, right)
        cnt += merge(A, left, mid, right)
    return cnt


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    A = il()
    cnt = merge_sort(A, 0, N)
    print(*A)
    print(cnt)


if __name__ == '__main__':
    main()

