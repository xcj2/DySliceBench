#!/usr/bin/env python3
import sys
import math
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10**8)
INF = float("inf")

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]", B: "List[int]"):
    # 直交するイワシは選べない。
    # 順にイワシを見て、直行するものをグループにする。
    # 先に単純な整数比へ変換しておく（有理数としての扱い）
    # aは整数、bは非負整数となるように整理する
    d = Counter()
    # (a, b) == (0, 0)については、他のイワシと同時に選ぶことができない。
    # 個別にカウントする。
    kodokunaiwashi = 0
    for i, (a, b) in enumerate(zip(A, B)):
        if a == 0 and b == 0:
            kodokunaiwashi += 1
        elif b == 0:
            d[1, 0] += 1
        elif b > 0:
            g = math.gcd(b, a)
            aa = a//g
            bb = b//g
            d[aa, bb] += 1
        else:
            g = math.gcd(-b, -a)
            aa = -a//g
            bb = -b//g
            d[(aa, bb)] += 1

    # 直交するグループを考える。
    ans = 1
    for a, b in d:
        # (a, b)と直交するのは、(-b, a)と(b, -a)である。
        # このうち、有理数としてカウントしている方を採用する
        x, y = -b, a
        if y < 0:
            x = -x
            y = -y
        elif y == 0:
            x = abs(x)

        # すでに直交するイワシとしてカウントをしたらNoneとしている。
        if d[a, b] == None:
            continue

        if d[x, y] == 0:
            # 直交するイワシが存在しない場合、自由に選ぶことができる。
            ans *= pow(2, d[a, b], MOD)
            ans %= MOD
            continue
        else:
            # 直交するイワシが存在する場合、どちらかのグループから自由に選ぶ。
            # ただし、一つも選ばないという場合は、重複するためケア
            buf = pow(2, d[a, b], MOD)
            buf += pow(2, d[x, y], MOD)
            buf -= 1
            buf %= MOD
            # print(buf)
            ans *= buf
            ans %= MOD
            d[x, y] = None

    print((ans-1+kodokunaiwashi) % MOD)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


if __name__ == '__main__':
    main()
