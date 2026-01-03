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

n,m = li()
stu = []
for _ in range(n):
    stu.append(tuple(li()))
chk = []
for _ in range(m):
    chk.append(tuple(li()))
    
for s in stu:
    ans_cand = []
    for c in chk:
        ans_cand.append(abs(c[0] - s[0]) + abs(c[1] - s[1]))
    
    ans = min(ans_cand)
    print(ans_cand.index(ans) + 1)