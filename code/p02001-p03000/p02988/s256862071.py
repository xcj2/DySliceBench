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

# import numpy as np
# from scipy.special import perm
# from scipy.special import comb

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

########

# S = input()

# c = Counter(S)

# flag = True
# for i in c.values():
#     if i != 2:
#         flag = False

# if flag:
#     print("Yes")
# else:
#     print("No")

n = i_inpl()
p = l_inpl()

cnt = 0
for i in range(n-2):
    G = [p[i], p[i+1], p[i+2]]
    G.sort()
    if G[1] == p[i+1]:
        cnt += 1

print(cnt)