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

# ここから処理
s = ns()
k = ni()

chl = list(s)
res = k

for i, c in enumerate(chl):
    if c == "a":
        continue
    
    elif res >= ord("z") - ord(c) + 1:
        chl[i] = "a"
        res -= (ord("z") - ord(c) + 1)

chl[-1] = chr(ord(chl[-1]) + res%26)

print("".join(chl))