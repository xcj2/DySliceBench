#!/usr/bin/python3
# import bisect
# from collections import Counter, deque, OrderedDict, defaultdict
# from copy import copy, deepcopy # pythonのみ．copyは1次元，deepcopyは多次元．
# from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
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
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    """
    https://qiita.com/drken/items/4a7869c5e304883f539b#3-3-dfs-%E3%81%AE%E5%86%8D%E5%B8%B0%E9%96%A2%E6%95%B0%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E5%AE%9F%E8%A3%85
    cf. https://atcoder.jp/contests/abc138/submissions/13273052
    """
    
    from collections import deque
    
    
    N, M = map(int, input().split())  # 頂点数，辺数
    # グラフ入力受取 (ここでは無向グラフを想定)
    G = [[] for _ in range(N)]


    for i in range(M):
        l, r,d = map(int, input().split())
        l-=1
        r-=1
        G[l].append((r,d))
        G[r].append((l,-d))
    
    seen = [False]*N
    ans = [0]*N
    
    
    def dfs(G, v):
    
        # (根の親番号が必要なときは-1とする)
    
        seen[v] = True
        stack = deque([v])
        while stack:
            v = stack.pop()
            for next_v,cost in G[v]:
                if not seen[next_v]:
                    ans[next_v] =ans[v]+cost
                else:
                    if ans[next_v] !=ans[v]+cost:
                        return 'No'
                    else: continue

                seen[next_v] = True
                stack.append(next_v)
    
    
    def main():
        for i in range(N):
            if not seen[i]:
                if dfs(G,i)=='No':
                    return 'No'
                    break
                else:
                    continue
        return 'Yes'
    print(main())
    
    
resolve()