import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
# 解説を見てしまったので、せめて再帰ではない方法で
def main():
    n = int(input())
    m = 1 << n  # 総組合せ数
    aa = LLI(n)
    dp = [0] * m
    for s in range(3, m):
        # sのうさぎたちが1グループだった場合
        value = 0
        jj = []
        for i,aai in enumerate(aa):
            if not s & 1 << i: continue
            value += sum(aai[j] for j in jj if s & 1 << j)
            jj.append(i)
        # 部分集合tとその補集合に分かれる場合
        # 全体集合sから始めて、「1を引く」「sと論理積をとる」を繰り返すことで
        # すべての部分集合を列挙できる
        t = (s - 1) & s
        while t > 0:
            value_div = dp[t] + dp[s ^ t]
            if value_div > value: value = value_div
            t = (t - 1) & s
        dp[s] = value
    print(dp[m - 1])

main()
