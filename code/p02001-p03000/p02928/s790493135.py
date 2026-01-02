import math
import copy
from operator import mul
from functools import reduce
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
# 一次元累積和
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop

import re
# import numpy as np
# from scipy.misc import comb

# 再帰がやばいとき
import sys
sys.setrecursionlimit(10**9)

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
def line_inpl(x): return [i_inpl() for _ in range(x)]

INF = int(1e30)
MOD = int(1e9)+7 # 10^9 + 7

# field[H][W]
def create_grid(H, W, value = 0):
    return [[ value for _ in range(W)] for _ in range(H)]

########

def count_inversion(sequence):
    count = 0
    for i in range(1,len(sequence),1):
        for j in range(i,len(sequence),1):
            if sequence[i-1] > sequence[j]:
                count += 1
    return count

def power_func(a,n,p):
  bi=str(format(n,"b"))#2進表現に
  res=1
  for i in range(len(bi)):
    res=(res*res) %p
    if bi[i]=="1":
      res=(res*a) %p
  return res

def main():
    N, K = l_inpl()
    A = l_inpl()
    a1 = count_inversion(A)
    b1 = (count_inversion(A*2) - count_inversion(A))
    b2 =  (count_inversion(A*3) - count_inversion(A*2))
    c1 = b2 - b1
    print((a1*K+c1*(K%MOD)*((K-1)%MOD)//2)%MOD)

if __name__ == "__main__":
    main()
