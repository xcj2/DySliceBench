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

H, W = l_inpl()
field = [ input() for _ in range(H) ]
sy, sx = 0, 0
gy, gx = H-1, W-1
def bfs(field, number_of_moves, sy, sx):
    queue = deque([[sy, sx]])
    number_of_moves[sy][sx] = 0
    while queue:
        y, x = queue.popleft()
        current_number_of_move = number_of_moves[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if inside(ny, nx, H, W) and \
                field[ny][nx] == "." and \
                number_of_moves[ny][nx] == -1:
                number_of_moves[ny][nx] = current_number_of_move + 1
                queue.append([ny, nx])
    return number_of_moves

number_of_moves = [ [-1] * W for _ in range(H) ]
number_of_moves = bfs(field, number_of_moves, sy, sx)
b_cnt = sum([ f.count("#") for f in field])

if number_of_moves[gy][gx] == -1:
    print(-1)
else:
    print(H*W-b_cnt-number_of_moves[gy][gx]-1)