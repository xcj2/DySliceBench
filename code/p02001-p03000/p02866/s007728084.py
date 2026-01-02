# import bisect
import unittest
from io import StringIO
# https://note.nkmk.me/python-scipy-connected-components/
from collections import Counter, deque
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
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    def main():
        n = int(input())
        D = list(map(int, input().split()))
        cnts=[0]*(max(D)+1)
        for i in D:
            cnts[i]+=1

        if cnts[0]!=1 or D[0]!=0: return 0
        ans=1

        for i in range(2,max(D)+1):
            if cnts[i]==0:
                return 0
            ans*=cnts[i-1]**cnts[i]

        return ans % 998244353

    print(main())

# 
resolve()