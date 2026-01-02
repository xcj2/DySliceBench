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

n = ni()
h = list(li())
h.append(0)

# 非ゼロの左端を選んでいるか
haveleft = False
ans = 0

while any([hk > 0 for hk in h]):
    for k in range(len(h)):
        if not haveleft:
            if h[k] == 0:
                continue
            else:
                haveleft = True
                h[k] -= 1
                
        else:
            if h[k] == 0:
                ans += 1
                haveleft = False
            else:
                h[k] -= 1
            
print(ans)