# import bisect
from collections import Counter, deque # https://note.nkmk.me/python-scipy-connected-components/
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
        s=str(input())
        s=deque(iterable=s)
        cnt=0
        if len(s)==1:
            return 0
        else:
            while len(s)>=2:
                sl=s.popleft()
                sr=s.pop()
                if sl==sr:
                    continue
                elif sl!='x' and sr!='x':
                    return -1
                elif sl!='x':
                    s.appendleft(sl)
                    s.append(sr)
                    s.appendleft('x')
                    cnt+=1
                else:
                    s.append(sr)
                    s.appendleft(sl)
                    s.append('x')
                    cnt+=1
            return cnt
    print(main())









resolve()