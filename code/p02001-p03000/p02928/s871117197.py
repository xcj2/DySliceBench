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
    n, k = LI()
    a_s = LI()
    ts = [0 for i in range(n)]
    f_ts = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if a_s[j] < a_s[i]:
                ts[i] += 1
                if j > i:
                    f_ts[i] += 1
    sum_f = sum(f_ts)
    sum_ = sum(ts)
    if (k - 1) % 2 == 0:
        ans = (sum_f + int(sum_ * (k - 1) / 2)) % MOD
        print(int(ans) % MOD * k % MOD)
    else:
        ans = 2 * sum_f + sum_ * (k - 1) % MOD
        print(int(ans) % MOD * int(k / 2) % MOD)


if __name__ == "__main__":
    main()
