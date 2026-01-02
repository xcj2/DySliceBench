from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
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


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


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

def bfs(graph, initial):
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
                q.append(e)
                dist[e] = dist[edge] + 1
                visited[e] = True

    return dist


def main():
    N, M = MI()

    ret = bfs(graph, 1)
    print(ret)


def main():
    N, X, Y = MI()
    graph = [[] for i in range(N+1)]

    for i in range(1, N):
        graph[i].append(i+1)
        graph[i+1].append(i)

    graph[X].append(Y)
    graph[Y].append(X)

    d = defaultdict(int)
    for i in range(1, N+1):
        ret = bfs(graph, i)
        for j in range(1, len(ret)):
            if i != j:
                d[ret[j]] += 1
        # print(ret)

    # print(d)
    for i in range(1, N):
        if i in d:
            print(d[i]//2)
        else:
            print(0)
    # d = defaultdict(int)

    # for i in range(1, N+1):
    #     for j in range(i+1, N+1):
    #         a = abs(j - i)
    #         b = abs(X - i) + 1 + abs(Y - j)
    #         c = abs(Y - i) + 1 + abs(X - j)
    #         d[min(a, b, c)] += 1

    # for i in range(1, N):
    #     if i in d:
    #         print(d[i])
    #     else:
    #         print(0)


if __name__ == '__main__':
    main()
