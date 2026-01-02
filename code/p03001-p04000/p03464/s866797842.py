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
 
def judge(k:int, a:list):
    mi = ma = 2
    for ai in a[::-1]:
        # miをaiの倍数に切り上げる
        if mi%ai:
            mi = -(-mi//ai) * ai
            
        # maをaiの倍数-1に切り上げる
        ma = (ma//ai + 1) * ai - 1

        if ma < mi:
            return False, (-1,-1)
        
    return True, (mi,ma)
 
k = ni()
a = list(li())
 
tf, (mi,ma) = judge(k,a)
if tf:
    print(mi,ma)
else:
    print(-1)
    