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

d,g = li()
pc = []
for _ in range(d):
    pc.append(tuple(li()))
    
ans = 10**10
for bit in range(1<<d):
    point = 0
    probs = 0
    for b in range(d):
        if bit & (1<<b):
            point += (100*(b+1)*pc[b][0] + pc[b][1])
            probs += pc[b][0]
            
    if point >= g:
        ans = min(ans, probs)
           
    else:

        res = g-point
        for q in range(d-1, -1, -1):
            if bit & (1<<q):
                continue
            
            if 100*(q+1)*(pc[q][0]-1) >= res:
                probs += -(-res // (100*(q+1)))
                res = 0
                
            else:
                res -= 100*(q+1)*(pc[q][0]-1)
                probs += pc[q][0]
        
        if res == 0:        
            ans = min(ans,probs)

            
print(ans)