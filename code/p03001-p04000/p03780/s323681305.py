import sys

def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,K = MI()
A = LI()
A.sort()


def f(n):  # Anが必要か否か
    B = [0] + [A[i] for i in range(N) if i != n]
    dp = [[0]*K for _ in range(2)]  # dp[i][j] = B1~Biを用いてjを作れるか(メモリ節約のため工夫してる)
    dp[0][0] = 1
    for i in range(1,N):
        b = B[i]
        for j in range(K):
            if j >= b:
                dp[i%2][j] = dp[1-i%2][j] | dp[1-i%2][j-b]
            else:
                dp[i%2][j] = dp[1-i%2][j]
    if sum(dp[(N-1) % 2][j] for j in range(max(K-A[n],0),K)) != 0:
        return True
    else:
        return False


left = -1  # 不必要
right = N  # 必要
while left + 1 < right:
    mid = (left + right)//2
    if f(mid):
        right = mid
    else:
        left = mid

print(right)
