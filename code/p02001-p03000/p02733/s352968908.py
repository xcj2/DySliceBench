import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

h,w,k = get_nums_l()
grid = [ input() for _ in range(h)]

ruiseki_white = [ [0] * (w+1) for _ in range(h) ]
for y in range(h):
    for x in range(w):
        ruiseki_white[y][x+1] = ruiseki_white[y][x] + (1 if grid[y][x] == "1" else 0)

# log(ruiseki_white)

def num_whites(l,r,t,b):
    ret = 0
    for y in range(t, b):
        ret += ruiseki_white[y][r] - ruiseki_white[y][l]
    # log(l,r,t,b,ret)
    return ret

ans = 999999999999999999

for bits in range(2**(h-1)):
    h_breaks=[0]
    for i in range(h-1):
        if bits &  2**i != 0:
            h_breaks.append(i+1)
    h_breaks.append(h)

    # log("h_breaks: ", h_breaks)

    w_break_count = 0
    prev_w_break = 0
    ok = True
    for x in range(1,w+1):
        for i in range(len(h_breaks) - 1):
            top = h_breaks[i]
            bottom = h_breaks[i+1]
            left = prev_w_break
            right = x
            if num_whites(left, right, top, bottom) > k:
                # ここの左で切る
                # log("CUT", left, right, top, bottom)
                if prev_w_break + 1 == x:
                    # この縦の切り方はだめ
                    ok = False
                prev_w_break = x-1
                w_break_count += 1
                break
        if not ok:
            break
    if ok:
        # log("ok. wbreak_count: ", w_break_count)
        ans = min(ans, len(h_breaks)-2 + w_break_count)

print(ans)