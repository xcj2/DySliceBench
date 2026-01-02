import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))

def gcd(a, b):
    if b == 0: return a
    if (a, b) in memo: return memo[(a, b)]
    res = memo[(a, b)] = gcd(b, a % b)
    return res
memo = {}

def main():
    md = 10 ** 9 + 7
    h, w, t = MI()
    # t=1のパターンに置き換える
    h1 = h // gcd(h, t)
    w1 = w // gcd(w, t)
    ans = (pow(2, h1, md) + pow(2, w1, md) + pow(2, gcd(h1, w1), md) - 3) % md
    # print(ans)
    # t=1のパターンの個数分累乗
    ans = pow(ans, gcd(h, t) * gcd(w, t), md)
    print(ans)

main()
