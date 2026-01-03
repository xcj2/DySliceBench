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
a = li()

# 各数のindexを格納
dic = {}
for i, ai in enumerate(a):
    dic[ai] = i
    
# 各indexに対して、左端のindexをleft, 右端のindexをrightに格納する
left = list(range(n+2))
right = list(range(n+2))

ans = 0
for i in range(n,0,-1):
    idx = dic[i]
    ans += i * (right[idx] - idx + 1) * (idx - left[idx] + 1)
    right[left[idx] - 1] = right[idx]
    left[right[idx] + 1] = left[idx]

print(ans)