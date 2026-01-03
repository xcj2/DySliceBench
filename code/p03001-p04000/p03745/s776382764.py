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

a_diff = []
ans = 1
for i in range(n-1):
    a_diff.append(a[i+1] - a[i])
    
cur = 0
for i in range(n-1):
    if cur == 0:
        if a_diff[i] == 0:
            continue
        elif a_diff[i] > 0:
            cur = +1
        else:
            cur = -1
            
    elif cur == +1:
        if a_diff[i] >= 0:
            continue
        else:
            cur = 0
            ans += 1
            
    elif cur == -1:
        if a_diff[i] <= 0:
            continue
        else:
            cur = 0
            ans += 1
            
    else:
        print("バグってます／(^o^)＼")
            
        
print(ans)