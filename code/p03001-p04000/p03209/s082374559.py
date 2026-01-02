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

n,x = li()

top = [4*pow(2,i) - 3 for i in range(n+1)]
med = [pow(2,i+1) - 1 for i in range(n+1)]
bot = [1 for _ in range(n+1)]

def findPattyNum(level:int, lay: int):
    if level == 0 and lay == 1:
        return 1
    
    if lay == 4*pow(2,level)-3:
        return pow(2,level+1) - 1
    
    elif pow(2,level+1)-1 < lay < 4*pow(2,level)-3:
        return pow(2,level) + findPattyNum(level-1, lay - (pow(2,level+1)-1))
    
    elif lay == pow(2,level+1)-1:
        return pow(2,level)
    
    elif 1 < lay < pow(2,level+1)-1:
        return findPattyNum(level-1, lay-1)
    
    elif lay == 1:
        return 0
    
print(findPattyNum(n,x))