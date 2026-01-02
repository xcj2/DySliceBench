"""
task statement
==============

長さ N の整数の列 A_1,A_2,\ldots,A_N であって以下の条件をすべて満たすものはいくつありますか。

0 \leq A_i \leq 9
A_i=0 なる i が存在する。
A_i=9 なる i が存在する。

ただし、答えはとても大きくなる可能性があるので、10^9+7 で割った余りを出力してください。

io_style
-------
N
"""
import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    if n == 1:
        print(0)
        return
    MOD = 10**9 + 7
    ans = pow(10, n, MOD) - pow(9, n, MOD) - pow(9, n, MOD) + pow(8, n, MOD)
    print(ans % MOD)
    return


if __name__ == "__main__":
    main()
