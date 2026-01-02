from collections import Counter, deque, OrderedDict
# from copy import copy, deepcopy
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import statistics # Pythonのみ
# import string
import unittest
from io import StringIO
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    N, Q = map(int, input().split())
    M = N-1  # 頂点数，辺数
    ans = [0]*N

    # グラフ入力受取 (ここでは無向グラフを想定)
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    for i in range(Q):
        p, x = map(int, input().split())
        p -= 1
        ans[p] += x

    seen = [False]*N

    def dfs(G, v):
        seen[v] = True
        stack = deque([v])
        while stack:
            v = stack.pop()
            for next_v in G[v]:
                if seen[next_v]:
                    continue
                seen[next_v] = True
                ans[next_v] += ans[v]
                stack.append(next_v)

    # 頂点 0 をスタートとした探索
    dfs(G, 0)
    print(*ans)


resolve()