import math
import copy
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
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")
MAX_DIGIT = 50

############
############
############

Q = i_inpl()
l, r = [], []

max_r = -INF
for _ in range(Q):
    li, ri = l_inpl()
    l.append(li)
    r.append(ri)
    max_r = max(max_r, ri)

MAX_X = 100030
prime_table = [True] * MAX_X
prime_table[0] = prime_table[1] = False

for (i, is_prime) in enumerate(prime_table):
    if is_prime:
        for n in range(i*i, MAX_X, i):
            prime_table[n] = False

# 1は2017に似てない数字
cumsums = [0]
for odd in range(3, max_r+3, 2):
    tmp = 0
    if prime_table[odd] and prime_table[(odd+1)//2]:
        tmp += 1
    cumsums.append(cumsums[-1] + tmp)

for li, ri in zip(l, r):
    if li > 1:
        li = li//2 - 1
    else:
        li = 0
    ri = ri//2
    print(cumsums[ri]-cumsums[li])
