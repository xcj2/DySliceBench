import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**8) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n,m = li()
ball = [1]*n
inred = [0]*n
inred[0] = 1

for _ in range(m):
    x,y = li_()
    if inred[x] and ball[x] == 1:
        inred[x] = 0
        ball[x] = 0
        
        inred[y] = 1
        ball[y] += 1
        
    elif inred[x] and ball[x] > 1:
        ball[x] -= 1
        
        inred[y] = 1
        ball[y] += 1
        
    else:
        ball[x] -= 1
        ball[y] += 1
        
ans = 0
for ri in inred:
    ans += ri
print(ans)
