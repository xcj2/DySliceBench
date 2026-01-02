from sys import stdin, gettrace
import sys
 
if not gettrace():
    def input():
        return next(stdin)[:-1]
 
 
# def input():
#    return stdin.buffer.readline()
 
def mincost(n,h,k):
  dp=[-1 for i in range(n)]
  dp[n-1]=0
  dp[n-2]=abs(h[n-2]-h[n-1])
  for i in range(n-3,-1,-1):
    mn=min(i+k+1,n)
    mnm=sys.maxsize
    for j in range(i+1,mn):
      mnm=min(dp[j]+abs(h[j]-h[i]),mnm)
    dp[i]=mnm    
  return dp[0]
 
def main():
  n,k=map(int,input().split())
  h=[int(x) for x in input().split()]
  print(mincost(n,h,k)) 
 
if __name__ == "__main__":
    main()