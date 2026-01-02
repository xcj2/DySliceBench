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

n,k = li()

ab = []
for _ in range(n):
    a,b = li()
    if a <= k:
        ab.append((a,b))

binn = len(bin(k))-2
bink = bin(k)[2:]

# binの候補を挙げる
cands = [bink]
for i, s in enumerate(list(bink)):
    if int(s):
        cands.append(bink[:i] + "0" + "1"*(binn-i-1))
        
ans = 0
for cand in cands:
    tmp = 0    
    cand = int("0b"+cand, 0)
    
    for a, b in ab:

        if cand | a <= cand:
            tmp += b
                
    ans = max(ans, tmp)
    
print(ans)