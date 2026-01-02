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
xyh = []
for _ in range(n):
    xyh.append(tuple(list(li())))

def search_cent(xyh:list):    
    xmax ,ymax, hmax = -1, -1, -1
    for x,y,h in xyh:
        if h > hmax:
            xmax = x
            ymax = y
            hmax = h
            
    for x_cent in range(101):
        for y_cent in range(101):
            h_cent = hmax + abs(xmax-x_cent) + abs(ymax-y_cent)
            
            # 矛盾チェック
            is_cent = True
            for x,y,h in xyh:
                hi = max(0, h_cent - abs(x-x_cent) - abs(y-y_cent))
                
                if hi != h:
                    is_cent = False
                    break

            if is_cent:
                return x_cent, y_cent, h_cent
        
xc, yc, hc = search_cent(xyh)
print(xc,yc,hc)