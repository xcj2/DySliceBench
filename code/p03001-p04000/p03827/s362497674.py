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

n = ni()
s = lc()

res = 0
ans = 0
for c in s:
    if c == "I":
        res += 1
        
        if res > ans:
            ans = res
            
    elif c == "D":
        res -= 1
        
print(ans)