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
f = [int("".join(ls()), 2) for _ in range(n)]      
p = [list(li()) for _ in range(n)]

def dfs(cur:int, depth:int):
    if depth == 10:
        if cur == 0:
            return -float("inf")
        else:
            return sum([p[i][bin(cur&fi).count("1")] for i, fi in enumerate(f)])
    
    else:
        return max(dfs(cur+(1<<depth), depth+1),
                   dfs(cur, depth+1))
        
print(dfs(0,0))