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


def MI(): return map(int, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def main():
    BLACK = '#'
    WHITE = '.'
    H, W = MI()
    graph = [[0 for i in range(W)] for i in range(H)]
    ans = 0
    options = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(H):
        S = input()

        for j in range(W):
            graph[i][j] = S[j]

    if H == 1 and W == 1:
        print(0)
        return

    if (H == 2 and W == 1) or (H == 1 and W == 2):
        print(1)
        return

    # H = 2
    # W = 2
    # graph = [['.' for i in range(W)] for i in range(H)]

    ans = 0
    for h in range(H):
        for w in range(W):
            if graph[h][w] == BLACK:
                continue

            visited = [[False for i in range(W)] for i in range(H)]
            q = deque()
            q.append(((h, w), 0))
            arr = []
            while len(q) != 0:
                p, c = q.popleft()
                # print(ans, n)

                for d in options:
                    i = p[0] + d[0]
                    j = p[1] + d[1]

                    if i >= 0 and i < H and j >= 0 and j < W and not visited[i][j] and graph[i][j] == WHITE:
                        visited[i][j] = True
                        q.append(((i, j), c+1))
                        # print((i, j), c+1)
                    else:
                        arr.append(c)
            # print(h, w, arr, max(arr))
            ans = max(ans, max(arr))

    print(ans)



if __name__ == '__main__':
    main()
