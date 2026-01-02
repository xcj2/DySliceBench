import sys


sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def factorization(N):
    d = {}
    for n in range(2, N + 1):
        tmp = n
        for i in range(2, int(n ** 0.5) + 1):
            if tmp % i == 0:
                cnt = 0
                while tmp % i == 0:
                    cnt += 1
                    tmp //= i
                if i not in d:
                    d[i] = cnt
                else:
                    d[i] += cnt

        if tmp != 1:
            if tmp not in d:
                d[tmp] = 1
            else:
                d[tmp] += 1

    return d


def main():
    N = int(input())
    d = factorization(N)
    d = [v for k, v in d.items() if v > 1]
    cnt = {2: 0, 4: 0, 14: 0, 24: 0, 74: 0}
    cnt[2] = len(d)
    for i in range(len(d)):
        val = d[i]
        if val >= 74:
            cnt[74] += 1
        if val >= 24:
            cnt[24] += 1
        if val >= 14:
            cnt[14] += 1
        if val >= 4:
            cnt[4] += 1

    ans = cnt[74]
    ans += cnt[24] * (cnt[2] - 1)
    ans += cnt[14] * (cnt[4] - 1)
    ans += cnt[4] * (cnt[4] - 1) // 2 * (cnt[2] - 2)

    print(ans)


if __name__ == "__main__":
    main()
