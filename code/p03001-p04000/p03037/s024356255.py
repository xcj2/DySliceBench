# -*- coding: utf-8 -*-
# IMPORT ###############################################################################################################
import sys                                                      # システム
# sys.setrecursionlimit(10**6)                                    # 再帰処理の上限変更
# from collections import deque, Counter                          # キュー・個数カウント
# from itertools   import accumulate, permutations, combinations  # 累積和・順列・組み合わせ
# from operator    import itemgetter                              # ソート補助
# from bisect      import bisect_left, bisect_right, bisect       # 二分探索
# from heapq       import heappop, heappush                       # プライオリティキュー
# from fractions   import gcd                                     # 最大公約数
# from math        import ceil, floor, sqrt, cos, sin, tan, pi    # 数学処理
# from copy        import deepcopy                                # オブジェクトコピー
# import numpy         as np                                      # 数値計算

# MAIN #################################################################################################################
def main():
    # Init #############################################################################################################
    im = InputManager()
    # Input ############################################################################################################
    n, m = im.inputMultiple()
    left = 0
    right = n
    for _ in range(m):
        l, r = im.inputMultiple()
        left = max(left, l - 1)
        right = min(right, r - 1)
    # Logic ############################################################################################################

    # Output ###########################################################################################################
    if (right - left) >= 0:
        print(right - left + 1)
    else:
        print(0)
    # Return ###########################################################################################################
    return

# INPUT MANAGER ########################################################################################################
class InputManager(object):
    def __init__(self):
        pass

    @staticmethod
    def inputSingle(dtype=int):
        return dtype(input())
    
    @staticmethod
    def inputMultiple(dtype=int, aslist=False):
        if aslist:
            return list(map(dtype, input().split()))
        else:
            return map(dtype, input().split())

    @staticmethod
    def input2D(h, dtype=int):
        return [list(map(dtype, input().split())) for i in range(h)]

# CALL MAIN ############################################################################################################
main()