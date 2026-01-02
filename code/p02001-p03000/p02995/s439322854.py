# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def gcd(a, b):
    """
    最大公約数を求める
    """
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    最小公倍数を求める
    """
    return a*b//(gcd(a, b))


def calc_num(n, C, D):
    """
    0~Nまでで、C or Dで割り切れない数の個数
    """

    div_C = n//C
    div_D = n//D
    div_CD = n//(lcm(C, D))
    return n-div_C-div_D+div_CD


def solve():
    A, B, C, D = map(int, input().split())
    return calc_num(B, C, D)-calc_num(A-1, C, D)


print(solve())
