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
    n = int(input())
    seq = [int(input()) for _ in range(n)][::-1]

    """
    Longest Increasing/Decreasing Subsuquence (LIS, LDS)
    Verified:
        https://atcoder.jp/contests/abc134/tasks/abc134_e
        https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/all/DPL_1_D
    """


    def longest_subsequence(A: "Array[int]", equals: bool, increasing: bool) -> int:
        """
        Compute the length of LIS or LDS.
        
        Args:
            A ("Array[int]"): a list or tuple to compute.
            equals (bool): permit adjacent numbers in subsequence to equal.
            increasing (bool): compute an increasing subsequence or decreasing one.
        Returns: (int) the length of a subsequence.
        """
        from bisect import bisect_left, bisect_right

        bs = bisect_right if equals else bisect_left
        compare = (lambda x, y: x >= y) if equals else (lambda x, y: x > y)
        if not increasing:
            A = A[::-1]

        dp = [A[0]]  # dp := length of LIS (dp table itself is not LIS)
        for i in A[1:]:
            if compare(i, dp[-1]):
                dp.append(i)
            else:
                dp[bs(dp, i)] = i
        return len(dp)
    
    print(longest_subsequence(seq,True,True))

    
    




resolve()