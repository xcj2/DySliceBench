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
hmax = 0
xmax = -1
ymax = -1
for _ in range(n):
    x,y,h = li()
    if h > hmax:
        hmax = h
        xmax = x
        ymax = y
        
    xyh.append((x,y,h))
    
xans = -1
yans = -1
hans = -1
flag = False
    
for x in range(101):
    for y in range(101):
        hcent = hmax + abs(xmax-x) + abs(ymax-y)
        consis = True
        
        for xi,yi,hi in xyh:
            if hi != max(0, hcent - abs(x-xi) - abs(y-yi)):
                consis = False
                
        if not consis:
            continue
                
        if consis:
            xans = x
            yans = y
            hans = hcent
            
            flag = True
            break
            
    if flag:
        break
            
            
print(xans, yans, hans)