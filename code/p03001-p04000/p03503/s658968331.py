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

def dfs(depth:int, inbis:str, f:list, p:list):
    if depth != 10:
        return max(dfs(depth+1, inbis+"1",f,p),
                   dfs(depth+1, inbis+"0",f,p))
        
    else:
        if inbis.count("1") == 0:
            return -10**10
        else:
            biz = [int(i) for i in inbis]
            ans = 0
            for i in range(len(f)):
                common = [biz[j]*f[i][j] for j in range(10)]
                ans += p[i][sum(common)]
                
            return ans

n = ni()
f = []
p = []
for _ in range(n):
    f.append(list(li()))
for _ in range(n):
    p.append(list(li()))
    
print(dfs(0,"",f,p))