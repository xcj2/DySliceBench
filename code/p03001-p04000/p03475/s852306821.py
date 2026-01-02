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
csf = [tuple(li()) for _ in range(n-1)]

for start in range(n-1):
    time = csf[start][1]
    for station in range(start,n-1):
        if time >= csf[station][1]:
            time = (-(-time//csf[station][2]))*csf[station][2]
            time += csf[station][0]
            
        else:
            time = csf[station][1]
            time += csf[station][0]
            
    print(time)
    
print(0)