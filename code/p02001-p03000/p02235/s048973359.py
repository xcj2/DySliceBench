# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja
# 最長共通部分文字列
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

# dp[i][j] := Sのi番目までとTのj番目までのLCS
# アルゴリズム的には正しいがTLE
def LCS(S, T):
    n = len(S)
    m = len(T)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n):
        S_i = S[i]
        for j in range(m):
            if S_i == T[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    
    return dp[n][m]


def LCS2(S, T):
    L = []
    for t in T:
        t_idx = 0  # 検索開始位置
        for i, cur_idx in enumerate(L):
            chr_idx = S.find(t, t_idx) + 1
            if not chr_idx:
                break
            L[i] = min(cur_idx, chr_idx)
            t_idx = cur_idx
        else:
            chr_idx = S.find(t, t_idx) + 1
            if chr_idx:
                L.append(chr_idx)
    
    return len(L)


def main():
    q = int(readline())
    xy = read().split()

    ans = []
    for X, Y in zip(*[iter(xy)]*2):
        ans.append(LCS2(X, Y))

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
