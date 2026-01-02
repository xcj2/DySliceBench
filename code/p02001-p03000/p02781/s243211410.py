import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

n,k = get_all_int()

# m桁の数値でf(n)=kとなる数の個数
# dp[k][m]
dp = [ [None]*101 for _ in range(4)]

for i in range(101):
    dp[0][i] = 1
dp[0][0] = 0
dp[1][0] = 0
dp[2][0] = 0
dp[3][0] = 0
dp[1][1] = 9
dp[2][1] = 0
dp[3][1] = 0

dp[1][2] = 1 * dp[1][1] + 9 * dp[0][1]
for i in range(2,101):
    dp[1][i] = 1 * dp[1][i-1] + 9 * dp[0][i-1]
    dp[2][i] = 1 * dp[2][i-1] + 9 * dp[1][i-1]
    dp[3][i] = 1 * dp[3][i-1] + 9 * dp[2][i-1]

# log(dp[1])
# log(dp[2])

ans = 0

keta = 0
x = n
while x > 0:
    keta += 1
    x //= 10

def sol(n, keta, k):
    if k == 0:
        return 1
    if k < 0:
        return 0
    if keta < k:
        return 0
    if keta == 0:
        return 1
    
    top = n//10**(keta-1)%10
    if keta==1:
        return top
    ans = 0
    # 0のとき
    if top == 0:
        ans += sol(n, keta-1, k)
    else:
        ans += 1 * (0 if keta==1 else dp[k][keta-1])
    # ans += sol(n, keta-1, k)
    log(keta,top,k,ans)

    # 1～top-1のとき
    if top != 0:
        if top == 1:
            ans += sol(n, keta-1, k-1)
        else:
            ans += (top-1) * (1 if keta==1 else dp[k-1][keta-1])
        # ans += (top-1) * sol(n, keta-1, k-1)
        log(keta,top,k,ans)

    # topのとき
    if top > 1:
        ans += sol(n, keta-1, k-1)
        log(keta,top,k,ans)
    return ans

if keta < k:
    print(0)
    exit()
ans += sol(n, keta, k)

print(ans)