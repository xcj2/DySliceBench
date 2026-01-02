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
    n = len(d)
    ans = 0
    for i in range(n):
        val = d[i]
        if val >= 74:
            ans += 1

        if val >= 24:
            ans += n - 1

        if val >= 14:
            cnt = 0
            for j in range(n):
                if i == j:
                    continue
                if d[j] >= 4:
                    cnt += 1
            ans += cnt

    cnt_4 = 0
    cnt_2 = 0
    for i in range(n):
        if d[i] >= 4:
            cnt_4 += 1
        else:
            cnt_2 += 1

    ans += (cnt_4 - 1) * cnt_4 // 2 * cnt_2
    ans += (cnt_4 - 2) * (cnt_4 - 1) * cnt_4 // 2

    print(ans)


if __name__ == "__main__":
    main()
