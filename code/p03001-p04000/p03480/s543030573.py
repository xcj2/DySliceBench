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

s = lc()
n = len(s)

fst = 0
lat = 0
ans = 0

if n % 2:
    fst = s[n//2::-1]
    lat = s[n//2:]
    ans = n//2 + 1

else:
    fst = s[n//2::-1]
    lat = s[n//2-1:]
    ans = n//2
  
for i in range(len(fst)-1):
    if fst[0] != lat[0]:
        break
    
    if fst[i+1] == fst[i] and lat[i+1] == lat[i]:
        ans += 1
        
    else:
        break
        
print(ans)