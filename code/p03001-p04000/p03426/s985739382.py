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
from bisect import bisect_left, bisect_right
# import numpy as np

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W
 
# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

########

H, W, D = l_inpl()
A = {}

for hi in range(H):
    l = l_inpl()
    for wi in range(W):
        A[l[wi]] = [wi, hi]

Q = i_inpl()
LR = []
for _ in range(Q):
    LRi = l_inpl()
    LR.append(LRi)

power = []
for i in range(1, H*W-D+1):
    power.append(abs(A[i+D][0] - A[i][0]) + abs(A[i+D][1] - A[i][1]))
    
r_cumsum = [0] * D
for i in range(len(power)):
    r_cumsum.append(r_cumsum[i] + power[len(power)-i-1])

cumsum = r_cumsum[::-1]

for l, r in LR:
    print(cumsum[l-1] - cumsum[r-1])