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

n,h = li()
alis = []
blis = []
for _ in range(n):
    a,b = li()
    alis.append(a)
    blis.append(b)
    
amax = max(alis)
blis.sort()
buse = []
while blis:
    cur = blis.pop()
    if cur > amax:
        buse.append(cur)
    
cnt = 0
res = h
for b in buse:
    res -= b
    cnt += 1
    if res <= 0:
        break
    
if res > 0:
    cnt += -(-res//amax)
    
print(cnt)