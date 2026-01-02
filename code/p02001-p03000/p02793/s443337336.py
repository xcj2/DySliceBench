import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
# INF = float("inf")


# 最大公約数
def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    n = int(input())
    A = list(map(int, input().split()))
    l = 1
    for a in A:
        l = lcm(l, a)
    c = 0
    for a in A:
        c += pow(a, MOD - 2, MOD)
    ans = l * c % MOD
    print(ans)


if __name__ == '__main__':
    main()
