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
    
    # https://qiita.com/drken/items/97e37dd6143e33a64c8c#3-%E3%82%81%E3%81%90%E3%82%8B%E5%BC%8F%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2%E3%81%AE%E3%81%95%E3%82%89%E3%81%AA%E3%82%8B%E5%88%A9%E7%82%B9

    n,a,b=map(int,input().split())
    h=[int(input()) for _ in range(n)]
    def is_ok(t):
        cnt=0
        for i in range(n):
            if h[i]-b*t>0:
                cnt+=math.ceil((h[i]-b*t) / (a-b))
        return cnt<=t

    def bin_search_meguru():
        """
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng, okは,とり得る最小の値-1,とり得る最大の値+1
        """
    
        # 適当にいじる
        ng = 0  # ind=0が条件を満たすこともあるため
        ok = 10**18  # ind=len(a)-1が条件を満たさないこともあるため
    
        # いじらない
        # okとngのどちらが大きいかわからないことを考慮
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    print(bin_search_meguru())
    

    
resolve()