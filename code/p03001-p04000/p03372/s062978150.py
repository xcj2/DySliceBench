import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from itertools import accumulate

n,c = li()
x_cw = []
v_cw = []
x_ccw = []
for _ in range(n):
    x,v = li()
    x_cw.append(x)
    v_cw.append(v)
    x_ccw.append(c-x)
    
x_ccw = [0] + sorted(x_ccw)
v_ccw = [0] + v_cw[::-1]
x_cw = [0] + x_cw
v_cw = [0] + v_cw
    
for i in range(1,n+1):
    v_cw[i] += (v_cw[i-1] - (x_cw[i]-x_cw[i-1]))
    v_ccw[i] += (v_ccw[i-1] - (x_ccw[i]-x_ccw[i-1]))
    
    
max_cw = [0]
max_ccw = [0]
mx_cw = [0]
mx_ccw = [0]
for i in range(1,n+1):
    max_cw.append(max(max_cw[-1], v_cw[i]))
    max_ccw.append(max(max_ccw[-1], v_ccw[i]))
    
    if max_cw[-1] != max_cw[-2]:
        mx_cw.append(x_cw[i])
    else:
        mx_cw.append(mx_cw[-1])

    if max_ccw[-1] != max_ccw[-2]:
        mx_ccw.append(x_ccw[i])
    else:
        mx_ccw.append(mx_ccw[-1])

ans = 0
for i in range(n+1):
    temp = max_cw[i] + max_ccw[n-i] - min(mx_cw[i], mx_ccw[n-i])
    ans = max(temp, ans)

        
print(ans)
