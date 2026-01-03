import math
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
        N,A,B=map(int,input().split())
        X=list(map(int,input().split()))
        if A>=B:
            return (N-1)*B
        else:
            ans=0
            merit=math.ceil(B/A)
            for i in range(N-1):
                d=X[i+1]-X[i]
                if d>=merit:
                    ans+=B
                else:
                    ans+=A*d
            return ans
    print(main())


    
resolve()