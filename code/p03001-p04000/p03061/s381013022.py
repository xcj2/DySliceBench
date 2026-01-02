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

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
    
n = ni()
a = list(li())
    
gcd_left = [0, a[0]]
gcd_right = [0, a[-1]]

for ai in a[1:]:
    gcd_left.append(gcd(gcd_left[-1], ai))
    
for ai in a[-2::-1]:
    gcd_right.append(gcd(gcd_right[-1], ai))
    
ans = 1

for le, ri in zip(gcd_left[:-1], gcd_right[::-1][1:]):
    if le == 0 or ri == 0:
        ans = max(ans, le, ri)
        
    else:
        ans = max(ans, gcd(le, ri))
        
print(ans)
    
