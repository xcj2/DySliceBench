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
            profit = 0
            for i,fi in enumerate(f):
                both = 0
                
                for mask in range(10):
                    if cur&(1<<mask) and fi&(1<<mask):
                        both += 1
                
                profit += p[i][both]
                
            return profit
    
    else:
        return max(dfs(cur+(1<<depth), depth+1),
                   dfs(cur, depth+1))
        
print(dfs(0,0))