# coding:utf-8
n = int(input())
h = list(map(int, input().split()))
dp = [float('inf')] * n

#後者が前者よりも小さい時に更新→DPテーブルをinfに初期化(先頭は0)
def chmin(a,b):
    if(a > b):
        return b
    else:
        return a

#後者が前者よりも大きい時に更新→DPテーブルを-infに初期化
def chmax(a,b):
    if(a< b):
        return b
    else:
        return a

def main():
    dp[0] = 0
    for i in range(1,n):
        dp[i] = chmin(dp[i], dp[i-1]+abs(h[i]-h[i-1]))
        if i > 1:
            dp[i] = chmin(dp[i], dp[i-2]+abs(h[i]-h[i-2]))
    
    print(dp[n-1])

if __name__ == '__main__' :
    main()