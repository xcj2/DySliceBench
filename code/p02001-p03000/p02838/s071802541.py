import sys
input = sys.stdin.readline

mod = 10 ** 9 + 7


def read_valus():
    return map(int, input().split())


def read_list():
    return list(read_valus())


def read_lists(N):
    return [read_list() for n in range(N)]


def p(N, a):
    return (a * (N - a)) % mod


def main():
    pows = [1] * 66
    for i in range(65):
        pows[i + 1] = (pows[i] * 2) % mod

    N = int(input())
    A = read_list()

    num = [0] * 65
    for a in A:
        tmp = a
        for i in range(65):
            if tmp == 0:
                break
            num[i] += tmp % 2
            tmp //= 2

    res = 0
    for i in range(65):
        if num[i] == 0:
            continue

        res = (res + (pows[i] * p(N, num[i])) % mod) % mod

    print(res % mod)


if __name__ == "__main__":
    main()
