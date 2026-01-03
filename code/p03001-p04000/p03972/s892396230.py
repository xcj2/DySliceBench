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


w,h = li()
stack = []
for _ in range(w):
    stack.append((ni(),0))
    
for _ in range(h):
    stack.append((ni(),1))
    
    
stack.sort(reverse=True)

res_w = 0
res_h = 0

ans = 0

while res_w <= w and res_h <= h and stack:
    cost, wh = stack.pop()

    if wh == 0:
        ans += (cost * ((h+1)-res_h))
        res_w += 1
        
    else:
        ans += (cost * ((w+1)-res_w))
        res_h += 1

        
print(ans)