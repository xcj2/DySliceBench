import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

MOD = 10**9+7

# X,Yに変換
n = ni()
s1 = lc()
s2 = lc()

xy = []

cnt = 0
while cnt < n:
    if s1[cnt] == s2[cnt]:
        xy.append("x")
        cnt += 1
    else:
        xy.append("y")
        cnt += 2
        
ans = 0

if xy[0] == "x":
    ans = 3
else:
    ans = 6
   
    
for pr,nx in zip(xy[:-1], xy[1:]):
    if pr == "x" and nx == "x":
        ans = (ans * 2) % MOD
        
    elif pr == "x" and nx == "y":
        ans = (ans * 2) % MOD
        
    elif pr == "y" and nx == "y":
        ans = (ans * 3) % MOD
        
print(ans)