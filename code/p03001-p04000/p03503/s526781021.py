import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def is_nth_bit_set(x, n):
    if x & (1 << n):
        return 1
    else:
        return 0


def main():
    N = int(input())
    F = []
    for _ in range(N):
        f = list(map(int, input().split()))
        F.append(f)

    P = []
    for _ in range(N):
        p = list(map(int, input().split()))
        P.append(p)

    ans = -INF
    total = 2 ** 10
    for pattern in range(1, total):
        joisino = [is_nth_bit_set(pattern, i) for i in range(10)]
        benefit = 0
        for f, p in zip(F, P):
            cnt = 0
            for i, j in zip(joisino, f):
                if i and j:
                    cnt += 1

            benefit += p[cnt]

        if ans < benefit:
            ans = benefit

    print(ans)


if __name__ == "__main__":
    main()
