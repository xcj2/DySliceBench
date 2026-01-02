from copy import copy, deepcopy # pythonのみ．1次元はcopy．多次元はdeepcopy
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
    def main():

        def next_permutation(a):
            """Generate the lexicographically next permutation inplace.

            https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
            Return false if there is no next permutation.
            """
            # Find the largest index i such that a[i] < a[i + 1]. If no such
            # index exists, the permutation is the last permutation
            for i in reversed(range(len(a) - 1)):
                if a[i] < a[i + 1]:
                    break  # found
            else:  # no break: not found
                return False  # no next permutation

            # Find the largest index j greater than i such that a[i] < a[j]
            j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

            # Swap the value of a[i] with that of a[j]
            a[i], a[j] = a[j], a[i]

            # Reverse sequence from a[i + 1] up to and including the final element a[n]
            a[i + 1:] = reversed(a[i + 1:])
            return True

        alpha = list(chr(ord('a')+i) for i in range(26))

        S = input()
        if len(S) < 26:
            for i in range(len(S)):
                alpha.remove(S[i])
            return S+alpha[0]
        else:
            S = list(S)
            P = S.copy()
            next_permutation(P)
            for i in range(26):
                if P[i] != S[i]:
                    return ''.join(P[:i+1])
            return -1
    print(main())

resolve()