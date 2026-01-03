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


aI, aO, aT, aJ, aL, aS, aZ = li()

if aI>0 and aJ>0 and aL>0:
    ans1 = 3 + ((aI-1)//2)*2 + ((aJ-1)//2)*2 + ((aL-1)//2)*2 + aO
    ans2 = (aI//2)*2 + (aJ//2)*2 + (aL//2)*2 + aO
    ans = max(ans1,ans2)

else:
    ans = (aI//2)*2 + (aJ//2)*2 + (aL//2)*2 + aO

print(ans)