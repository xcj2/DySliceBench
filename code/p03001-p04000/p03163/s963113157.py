from sys import stdin, gettrace
import sys
sys.setrecursionlimit(1000000)
if not gettrace():
    def input():
        return next(stdin)[:-1]
 
 
# def input():
#    return stdin.buffer.readline()

def recursion(li,i,n,w,dp):
    if i==n or w==0:
        return 0
    if li[i][0]>w:
        if dp[i+1][w]==-1:
            x=recursion(li,i+1,n,w,dp)
            dp[i+1][w]=x            
        else:
            x=dp[i+1][w]
        return x
    else:
        if dp[i+1][w]==-1:
            x=recursion(li,i+1,n,w,dp)
            dp[i+1][w]=x            
        else:
            x=dp[i+1][w]
        if dp[i+1][w-li[i][0]]==-1:
            y=recursion(li,i+1,n,w-li[i][0],dp)
            dp[i+1][w-li[i][0]]=y
        else:
            y=dp[i+1][w-li[i][0]]            
        return max(li[i][1]+y,x)

def main():
    n,w=[int(x) for x in input().split()]
    li=[]
    for i in range(n):
        temp=[int(x) for x in input().split()]
        li.append(temp)
    dp=[[-1 for j in range(w+1)] for i in range(n+1)]
    print(recursion(li,0,n,w,dp))
 
 
if __name__ == "__main__":
    main()