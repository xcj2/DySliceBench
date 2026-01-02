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

s = lc()
n = len(s)

if s[0] == "0" or s[-1] == "1" or s[-2] == "0":
    print(-1)
    
elif s[:(n-1)//2] != s[n-2:n//2-1:-1]:
    print(-1)
    
else:
    par = n
    cur = n-1
    print(n,n-1)
    
    if n > 2:
        for si in s[-3::-1]:
            cur -= 1
            print(par,cur)
            if si == "1":
                par = cur