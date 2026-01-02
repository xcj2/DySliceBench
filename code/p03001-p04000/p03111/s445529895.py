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

def choose3(bamboos: list, a: int, b: int, c: int):
    bamboos.sort(reverse=True)
    l = len(bamboos)
    minmp = float('inf')
    
    for idx in range(l):
        for jdx in range(idx+1,l):
            for kdx in range(jdx+1,l):
                minmp = min(minmp,
                            abs(bamboos[idx]-a)\
                             + abs(bamboos[jdx]-b)\
                             + abs(bamboos[kdx]-c))
    return minmp


def dfs(bamboos: list, a: int, b: int, c: int, mp: int):

    l = len(bamboos)
    
    if l == 3:
        return mp + choose3(bamboos, a, b, c)
    
    else:
        minmp = mp + choose3(bamboos, a, b, c)
        
        for p1 in range(l):
            for p2 in range(p1+1,l):
                newbamboos = [bamboos[p1] + bamboos[p2]]
                
                for p in range(l):
                    if p == p1 or p == p2:
                        continue
                    else:
                        newbamboos.append(bamboos[p])
                
                minmp = min(minmp, dfs(newbamboos, a, b, c, mp+10))
                del newbamboos
                
        return minmp
    
n,a,b,c = li()
laaa = [ni() for _ in range(n)]

print(dfs(laaa, a, b, c, 0))