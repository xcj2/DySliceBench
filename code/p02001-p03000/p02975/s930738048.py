# import bisect
from collections import Counter, deque  # https://note.nkmk.me/python-scipy-connected-components/
# from copy import copy, deepcopy
# from math import gcd
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
        N = int(input())
        A = list(map(int, input().split()))

        if all(a == 0 for a in A):
            return True
        if N % 3 != 0:
            return False

        AA = Counter(A)
        if len(AA) == 2:
            AAA = AA.most_common()
            if AAA[0][1] != N * 2 // 3:
                return False
            return AAA[1][0] == 0

        if len(AA) == 3:
            if any(v != N // 3 for v in AA.values()):
                return False
            k1, k2, k3 = AA.keys()
            return k1 ^ k2 == k3 or k1 ^ k3 == k2 or k2 ^ k3 == k1

    print('Yes' if main() else 'No')


resolve()