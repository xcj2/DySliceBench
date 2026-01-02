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

def print_lcs (a, b, lcs, i, j, cur):
    if i==0 or j==0:
        return cur
    
    elif a[i] == b[j]:
        ans = print_lcs(a,b,lcs,i-1,j-1,cur+a[i])
        return ans
    
    else:
        if lcs[i-1][j] >= lcs[i][j-1]:
            return print_lcs(a,b,lcs,i-1,j,cur)
        else:
            return print_lcs(a,b,lcs,i,j-1,cur)
        


s = " " + ns()
t = " " + ns()

lens = len(s)
lent = len(t)

lcs = [[0]*lent for _ in range(lens)]
ans = ""
for i in range(1,lens):
    for j in range(1,lent):
        if s[i] == t[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1

            
        else:
            if lcs[i-1][j] > lcs[i][j-1]:
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]
                
print(print_lcs(s,t,lcs,lens-1,lent-1,"")[::-1])