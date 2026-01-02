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


def insertion_sort(A, N, G):
    cnt = 0
    for i in range(G, N):
        v = A[i]
        j = i - G
        while j >= 0 and A[j] > v:
            A[j + G] = A[j]
            j = j - G
            cnt += 1
        A[j + G] = v
    return cnt


def shell_sort(A, N, G, m):
    cnt = 0
    for i in range(m):
        cnt += insertion_sort(A, N, G[i])
    return cnt


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    A = [ii() for _ in range(N)]

    G = [1]
    for i in range(N):
        g = G[i] * 3 + 1
        if g > N:
            break
        else:
            G.append(g)
    m = len(G)
    G = G[::-1]
    cnt = shell_sort(A, N, G, m)

    print(m)
    print(*G)
    print(cnt)
    print(*A, sep='\n')


if __name__ == '__main__':
    main()

