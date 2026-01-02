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
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def print_matrix(mat):
    for i in range(len(mat)):
        print(*['IINF' if v == IINF else "{:0=4}".format(v) for v in mat[i]])


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
show_flg = False
# show_flg = True

def bfs(graph, initial, MX):
    n = len(graph) - 1
    dist = [-1] * (n + 1)
    q = deque([initial])
    visited = [False] * (n + 1)
    visited[initial] = True
    dist = []

    while len(q) != 0:
        edge = q.popleft()
        nxt = graph[edge]
        dist.append(edge)

        if len(dist) == MX:
            return dist

        for i, e in enumerate(nxt):
            q.append(e)

    return dist


def main():
    N, K = MI()
    A = [i-1 for i in MI()]
    edges = [[] for i in range(N)]
    LIMIT = 3*10**5

    for i in range(N):
        edges[i].append(A[i])

    ret = bfs(edges, 0, LIMIT)
    m = defaultdict(int)
    loop_start = None
    loop_end = None
    for i in range(len(ret)):
        v = ret[i]
        if m[v] == 0:
            m[v] = i
        elif m[v] != 0:
            loop_start = m[v]
            loop_end = i - 1
            break
            # print(i)
    # print(ret[:5+1])

    if K <= LIMIT:
        print(ret[K]+1)
    else:
        # print(K % loop)
        # print(loop_start, loop_end)
        # org_K = K
        K -= loop_start
        loop_c = loop_end - loop_start + 1
        n_ret = ret[loop_start:]
        # print(n_ret[:15], 'loop_c',loop_c, 'K', K)
        print(n_ret[K % loop_c]+1)
        # print(ret[org_K]+1)
        # print(ret[:10])
        # print(ret[org_K])


if __name__ == '__main__':
    main()
