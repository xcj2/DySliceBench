import sys

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 18
MOD = 10 ** 9 + 7


def LI():
    return list(map(int, sys.stdin.readline().split()))


def II():
    return int(sys.stdin.readline())


def LS():
    return list(map(list, sys.stdin.readline().split()))


def S():
    return sys.stdin.readline()[:-1]


def main():
    m, d = LI()
    ans = 0
    for i in range(2, m + 1):
        for j in range(2, d + 1):
            if j < 20:
                continue
            jj = int(j / 10)
            jjj = j - 10 * jj
            if jjj < 2:
                continue
            if i == jj * jjj:

                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
