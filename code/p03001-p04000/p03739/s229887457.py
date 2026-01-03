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

# 正→負→正→...
cur = a[0]
ans_pn = 0
if cur <= 0:
    ans_pn = abs(a[0])+1
    cur = 1

for i in range(1,n):
    cur += a[i]
    if i%2 == 0 and cur <= 0:
        ans_pn += abs(cur)+1
        cur = 1
    elif i%2 == 1 and cur >= 0:
        ans_pn += abs(cur)+1
        cur = -1


# 負→正→負...
cur = a[0]
ans_np = 0
if cur >= 0:
    ans_np = abs(a[0])+1
    cur = -1

for i in range(1,n):
    cur += a[i]
    if i%2 == 0 and cur >= 0:
        ans_np += abs(cur)+1
        cur = -1
    elif i%2 == 1 and cur <= 0:
        ans_np += abs(cur)+1
        cur = 1
        

print(min(ans_np, ans_pn))