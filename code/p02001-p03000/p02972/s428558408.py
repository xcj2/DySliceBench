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

import re
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

ans = [0] * N
flag = True
for i in range(N)[::-1]:
    num = i+1
    cnt = N//num
    if cnt == 1:
        ans[i] = A[i]
    else:
        tmp = 0
        for j in range(1, cnt+1):
            tmp += ans[j*num-1]
        tmp %= 2
        if tmp == A[i]:
            ans[i] = 0
        elif tmp != A[i]:
            ans[i] = 1
        else:
            flag = False
            break
if flag:
    print(sum(ans))
    l = []
    for ind, i in enumerate(ans):
        if i != 0:
            l.append(str(ind+1))
    if sum(ans) != 0:
        print(" ".join(l))
else:
    print("-1")
