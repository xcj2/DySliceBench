from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product, combinations_with_replacement
import sys
import bisect
import string
import math
import time


def I(): return int(input())


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def debug(table, *args):
    ret = []
    for name, val in table.items():
        if val in args:
            ret.append('{}: {}'.format(name, val))
    print(' | '.join(ret), file=sys.stderr)


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True

ans = []

def bfs(graph, initial, H):
    global ans
    n = len(graph) - 1
    dist = [-1] * (n + 1)
    q = deque([initial])
    visited = [False] * (n + 1)
    visited[initial] = True
    dist[initial] = 0

    while len(q) != 0:
        edge = q.popleft()
        nxt = graph[edge]

        for i, e in enumerate(nxt):
            if visited[e] is False:
                if H[initial] <= H[e]:
                    return 0
                q.append(e)
                dist[e] = dist[edge] + 1
                visited[e] = True

    return 1


def main():
    global ans
    N, M = MI()
    H = LI()
    graph = [[] for i in range(N+1)]

    for i in range(M):
        a, b = MI()
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    ans = [-1] * N

    ret = 0
    for i in range(N):
        d = bfs(graph, i, H)
        print(i, d)
    print(ret)

def main():
    N, M = MI()
    H = LI()
    A = [0] * M
    B = [0] * M

    H_G = [-1 for i in range(N)]

    for i in range(M):
        A[i], B[i] = MI()

    for i in range(M):
        H_G[A[i]-1] = max(H_G[A[i]-1], H[B[i]-1])
        H_G[B[i]-1] = max(H_G[B[i]-1], H[A[i]-1])

    ans = 0

    for i in range(N):
        if H[i] > H_G[i]:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
