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

n = lc()
for i in range(8):
    cur = int(n[0])
    ans = n[0]
    for j in range(2,-1,-1):

        if (i>>j)&1 == 1:
            cur += int(n[3-j])
            ans = ans + "+" + n[3-j]
        else:
            cur -= int(n[3-j])
            ans = ans + "-" + n[3-j]
        
        
    if cur == 7:
        ans = ans + "=" + "7"
        break

print(ans)