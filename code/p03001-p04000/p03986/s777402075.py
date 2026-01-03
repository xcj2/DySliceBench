# 入力
import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

x = lc()

# Sを開きカッコ(, Tを閉じカッコ)のように考える
s_cnt = 0
ans = 0
for c in x:
    if c == "S":
        s_cnt += 1
    else:
        s_cnt -= 1
        
        if s_cnt < 0:
            ans += 1
            s_cnt = 0

ans += s_cnt

print(ans)