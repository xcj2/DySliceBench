# -*- coding: utf-8 -*-
from heapq import heapify, heappush, heappop
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy

sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]



def main(H, W, c_h, c_w, d_h, d_w):

    que = deque([(c_h, c_w)])
    INF = 1e9
    dist = [[INF]*W for _ in range(H)]
    dist[c_h][c_w] = 0
    while que:
        # print(que)
        tmp = que.popleft()
        h, w = tmp
        d = dist[h][w]
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            new_h = h + dy
            new_w = w + dx
            if new_h < 0 or H <= new_h or new_w < 0 or W <= new_w:
                continue
            if board[new_h][new_w] == '#':
                continue
            if dist[new_h][new_w] <= d:
                continue
            dist[new_h][new_w] = d
            que.appendleft((new_h, new_w))
        # 魔法
        for m_dy in range(-2, 3):
            for m_dx in range(-2, 3):
                new_h = h + m_dy
                new_w = w + m_dx
                if new_h < 0 or H <= new_h or new_w < 0 or W <= new_w:
                    continue
                if board[new_h][new_w] == '#':
                    continue
                if dist[new_h][new_w] <= d + 1:
                    continue
                dist[new_h][new_w] = d + 1
                que.append((new_h, new_w))

    ans = dist[d_h][d_w]
    if ans == INF:
        print(-1)
    else:
        print(ans)


H, W = zz()
c_h, c_w = zz()
d_h, d_w = zz()
board = []
c_h -= 1
c_w -= 1
d_h -= 1
d_w -= 1
for i in range(H):
    tmp = S()
    board.append(tmp)
main(H, W, c_h, c_w, d_h, d_w)
