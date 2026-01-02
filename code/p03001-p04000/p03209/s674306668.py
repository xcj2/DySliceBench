import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,X=map(int,input().split())
    
    memo=[(0,0)]*N
    memo[0]=(1,1)
    for i in range(N-1):
        memo[i+1]=(memo[i][0]*2+3,memo[i][1]*2+1)
    def saiki(n,x):
        if n==0:
            return 1 if x>0 else 0
        if memo[n-1][0]+2<x:
            return memo[n-1][1]+saiki(n-1,x-(memo[n-1][0]+2))+1
        elif memo[n-1][0]+2==x:
            return memo[n-1][1]+1
        else:
            return saiki(n-1,x-1)
    print(saiki(N,X))
        

if __name__ == '__main__':
    main()
