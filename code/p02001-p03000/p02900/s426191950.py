# 再帰関数の最大回数を増やす
import sys
sys.setrecursionlimit(1000000)

import math

def gcd(i, j):
    """
    2値 i, j の最大公約数を求める。
    """

    if j == 0:
        return i
    else:
        return gcd(j, i % j)

def factorize(n):
    """
    素因数分解した個数を返す
    """
    count = 1
    rep = math.ceil(math.sqrt(n))
    for i in range(2, rep + 1):
        if n % i != 0:
            continue
        else:
            count += 1
            while n % i == 0:
                n /= i
        if n == 1:
            return count
    if n != 1:
        count += 1
    return count

def main():
    a, b = map(int, input().split())

    #最大公約数を求める
    x = gcd(a, b)

    #最大公約数を素因数分解する
    count = factorize(x)

    #結果を出力する
    print(count)

main()