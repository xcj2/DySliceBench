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

def mera(n: int, hp:list, a:int, b:int) -> bool:
    hp = [hpi - n*b for hpi in hp]
    
    center = 0
    for hpi in hp:
        if hpi <= 0:
            continue
        else:
            center += (hpi//(a-b) + bool(hpi%(a-b)))

    if center > n:
        return False
    else:
        return True
    

n,a,b = li()
hp = [ni() for _ in range(n)]

# 二分探索
low = 0
high = max(hp)//b+1

while high - low > 1:
    mid = (high+low) // 2
    if mera(mid,hp,a,b):
        high = mid
    else:
        low = mid
        

print(high)
