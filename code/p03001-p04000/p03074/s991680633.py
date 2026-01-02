from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
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

        N, K = map(int, input().split())
        s = input()
        S = [int(c) for c in s]
        runlen = []
        if S[0] != 1:
            runlen.append(0)
        flag = False
        if S[-1] != 1:
            flag = True
        gr = groupby(S)
        cnt = 0
        for key, group in gr:  # groupはイテレータ。list(group)でリスト化
            runlen.append(len(list(group)))
            cnt += 1
        if flag:
            runlen.append(0)
        if cnt == 1:
            return N

        runlen = [0] + runlen
        # 累積和を格納したリスト．A[l:r]の総和はB[r] - B[l]
        runlen = list(accumulate(runlen))

        ans = 0
        for i in range(0,len(runlen),2):
            r = K*2+i+1
            l = i
            if r >= len(runlen):
                r = len(runlen)-1
            ans = max(ans, runlen[r]-runlen[l])

        return ans
    print(main())


resolve()