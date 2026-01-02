import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    rbl,gbl,bbl,n = LI()
    rmx = n//rbl
    ans = 0
    
    for r in range(rmx+1):
        gmx = (n-rbl*r)//gbl
        for g in range(gmx+1):
            reminder = n - (rbl*r+gbl*g)
            if reminder%bbl == 0:
                ans += 1
    
    print(ans)
main()            
