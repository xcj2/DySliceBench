"""

問題文:

制約:

解読:
- 2, 5はO(n)で求められるとのこと
  - 最後の桁がpで割り切れるかどうかのみで判定可能なため
  - solve1で、cntをi + 1でカウントしている理由:
    - 対象となる部分文字列は連続した部分文字列
    - iをインクリメントしながらカウント
    - i番目の数字を含む部分文字列のみカウントすればよい -> (i + 1)個
"""
n, p = map(int, input().split())
s = list(map(int, list(input())))
u = [0 for _ in range(n + 1)]

d = 1
for i in range(n):
    u[n-(i+1)] = (u[n-i] + s[n-i-1] * d) % p
    d = 10 * d % p


def solve(u, s, p):
    if 2 == p or 5 == p:
        return solve1(s, p)
    else:
        return solve2(u, p)


def solve1(s, p):
    ans = 0
    for i in range(n):
        if s[i] % p == 0:
            ans += i + 1
    return ans


def solve2(u, p):
    ans = 0
    cnt = [0 for _ in range(p)]
    for i in range(n + 1):
        cnt[u[i]] += 1
    for i in range(p):
        p = cnt[i]
        ans += (p * (p-1)) // 2
    return ans


print(solve(u, s, p))
