import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    S = list(input())
    k = input_int()

    # 方針: 左の文字から貪欲に a を作る
    #       余ったk は一番右の文字の操作につかう
    for i in range(len(S)):
        c = ord(S[i])
        if c == ord("a"):
            continue
        dif = ord("z") - c + 1
        if dif <= k:
            S[i] = "a"
            k -= dif
    # 余ったkを一番右の文字の操作に使う
    S[-1] = chr(ord("a") + ((ord(S[-1]) - ord("a")) + (k % 26)))
    print("".join(S))
    return


if __name__ == "__main__":
    main()
