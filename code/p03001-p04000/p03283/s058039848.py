import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,M,Q=mi()
    
    count = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        L,R=mi()
        count[L][R] += 1
    
    # print(count)
    dp = [[0] * (N+1) for _ in range(N+1)]

    for w in range(1,N+1):
        for h in range(1,N+1):
            l,r=N+1-w,h
            dp[w][h] += dp[w][h-1] + dp[w-1][h] - dp[w-1][h-1] + count[l][r]


    # print(dp)
    for i in range(Q):
        p,q=mi()
        w,h=N+1-p,q
        # print(w,h)
        print(dp[w][h])

            






if __name__ == "__main__":
    main()