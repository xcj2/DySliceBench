import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))
def fde(): print("-flag-")

def main():
    N=ii()
    A=list(mi())
    
    dp = [[0]*2 for _ in range(10**5+10)]
    dp[0][0] = A[0]+A[1]
    dp[0][1] = -dp[0][0]

    for i in range(1,N-1):
        dp[i][0]=max(dp[i-1][0]+A[i+1],dp[i-1][1]+A[i+1])
        dp[i][1]=max(dp[i-1][0]-2*A[i]-A[i+1],dp[i-1][1]+2*A[i]-A[i+1])
    
    print(max(dp[N-2]))



if __name__ == "__main__":
    main()