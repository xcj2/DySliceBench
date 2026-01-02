import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log

mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')
 
#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #int(input())
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii()) #list(map(int,input().split()))
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]
#文字列input
def ss(): return sys.stdin.readline().rstrip() #input()
def mss(): return sys.stdin.readline().rstrip().split()
def limss(): return list(mss()) #list(input().split())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

h,w=mii()

mat=[list(ss()) for _ in range(h)]

chk=[[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if i==0:
            if j==0:
                if mat[i][j]=="#":
                    chk[i][j]+=1
            else:
                if mat[i][j]!=mat[i][j-1] and mat[i][j]=="#":
                    chk[i][j]=chk[i][j-1]+1
                else:
                    chk[i][j]=chk[i][j-1]
        
        else:
            if j==0:
                if mat[i][j]!=mat[i-1][j] and mat[i][j]=="#":
                    chk[i][j]=chk[i-1][j]+1
                else:
                    chk[i][j]=chk[i-1][j]
            
            else:
                if mat[i][j]==mat[i-1][j] and mat[i][j]==mat[i][j-1]:
                    chk[i][j]=min(chk[i-1][j],chk[i][j-1])
                    
                elif mat[i][j]!=mat[i-1][j] and mat[i][j]==mat[i][j-1] and mat[i][j]=="#":
                    chk[i][j]=min(chk[i-1][j]+1,chk[i][j-1])
                elif mat[i][j]!=mat[i][j-1] and mat[i][j]==mat[i-1][j] and mat[i][j]=="#":
                    chk[i][j]=min(chk[i-1][j],1+chk[i][j-1])
                elif mat[i][j]=="#":
                    chk[i][j]=min(chk[i-1][j]+1,1+chk[i][j-1])
                else:
                    chk[i][j]=min(chk[i-1][j],chk[i][j-1])

                    
print(chk[-1][-1])
#print(chk)