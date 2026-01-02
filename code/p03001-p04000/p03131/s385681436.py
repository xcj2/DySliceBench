# https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_c
import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    k, a, b = input_int_list()
    if b - a <= 2:  # 2ターン 使って、作れるビスケットが2個以下だと最大化しない。
        ans = k + 1
    else:
        exchange, mod = divmod((k - (a - 1)), 2)
        ans = a
        ans += exchange * (b - a)
        ans += mod
    print(ans)

    return


if __name__ == "__main__":
    main()
