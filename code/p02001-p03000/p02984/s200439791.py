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
# from scipy.misc import perm
# from scipy.misc import comb

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
def line_inpl(x): return [i_inpl() for _ in range(x)]

INF = int(1e18)
MOD = int(1e9)+7 # 10^9 + 7

########

N = i_inpl()
A = l_inpl()

ans = []
tmp = 0
for i, Ai in enumerate(A[:N-1]):
    tmp += Ai *(-1)**(i)
a1 = (tmp+A[N-1])
ans.append(a1)
t_ans = []
r_A = A[::-1]
for i in range(N-1):
    ans.append(2*r_A[i]-ans[i])
ans = [ans[0]] + ans[1:][::-1]
print(" ".join([ str(i) for i in ans]))

# L, R = l_inpl()
# L %= 2019
# R %= 2019

# if R<=L:
#     R+=2019

# ans = INF
# for i in range(L, R+1):
#     for j in range(i+1, R+1):
#         print(i, j)
#         ans = min(ans, i*j%2019)

# print(ans)
