#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 2019  # type: int


def solve(L: int, R: int):
    lmod = L % MOD
    rmod = R % MOD
    if R-L > MOD:
        # すべて使えるので、0
        print(0)
        return
    elif rmod < lmod:
        # 0を使える
        print(0)
        return
    else:
        # 2019よりも小さいから、全探索が間に合う
        m = +INF
        for i in range(lmod, rmod+1):
            for j in range(i+1, rmod+1):
                curr = (i*j) % MOD
                if curr < m:
                    m = curr
                    # print(i, j, curr)
        print(m)
        return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(L, R)


if __name__ == '__main__':
    main()
