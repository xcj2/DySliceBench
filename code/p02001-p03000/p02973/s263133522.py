from bisect import bisect_right

def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD = 10 ** 9 + 7

N = I()
A = [I() for _ in range(N)]

# 広義単調減少列の長さの最大値を求めれば良い = Aを逆順に見ればLISと同値
# dp[i] := 長さがi以下の部分列で作られる広義単調減少列の最後の要素の最大値
dp = [-1]  # A[i] >= 0 なのでそれ以下の値を設定し、数列の単調性を保つ
for a in reversed(A):
    if dp[-1] <= a:
        dp.append(a)
    else:
        idx = bisect_right(dp, a)  # "広義"のため、同じ値が複数の場合は最も右のもの(right)
        dp[idx] = a
print(len(dp) - 1)
