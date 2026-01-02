def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0
def modinv(a, m):
    g, x, y = xgcd(a, m)
    return x % m
def main():
    s=list(input())
    mod=10**9+7
    K=modinv(10,13)
    U=[[0 for i in range(10) ]for k in range(13)]
    for i in range(13):
        for j in range(10):
            U[i][j]=((i-j)*K)%13

    dp=[[0 for k in range(13)] for i in range(len(s))]
    #dp[i][j]=初めのindex=i番目まで見たときに、あまりがjになるような方法の総数
    num=s[0]
    if s[0]=="?":
        for i in range(10):
            dp[0][i]=1
    else:
        number=int(s[0])
        dp[0][number]=1

    for i in range(1,len(s)):
        for k in range(13):
            if s[i]=="?":
                for j in range(10):
                    dp[i][k]+=dp[i-1][U[k][j]]%mod
            else:
                number=int(s[i])
                dp[i][k]=dp[i-1][U[k][number]]%mod
    print(dp[len(s)-1][5]%mod)
if __name__ == "__main__":
    main()