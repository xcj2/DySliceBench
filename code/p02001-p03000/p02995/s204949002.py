from math import factorial, ceil, floor # 階乗/切り上げ/切り捨て
from operator import itemgetter as ig
from collections import defaultdict as dd
# 定数
INF = float("inf")
MOD = int(1e9 + 7)
# 最大公約数 / 最小公倍数
def gcd(v1, v2):
    if v2 == 0:
        return v1
    return gcd(v2, v1 % v2)
def lcm(v1, v2):
    return (v1 // gcd(v1, v2)) * v2

# エントリーポイント
def main():
    A, B, C, D = map(int, input().split())
    def solve(v1, v2, d):
        return B // d - (A - 1) // d
    print((B - A + 1) - (solve(A, B, C) + solve(A, B, D) - solve(A, B, lcm(C, D))))

main()
