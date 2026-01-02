import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def is_nth_set(x, n):
    if x & (1 << n):
        return 1
    else:
        return 0


def main():
    N, M = map(int, input().split())
    S = []
    for _ in range(M):
        k, *s = map(int, input().split())
        s = [i - 1 for i in s]
        S.append(s)
    P = list(map(int, input().split()))

    ans = 0
    for pattern in range(2 ** N):
        switch = []
        for i in range(N):
            switch.append(is_nth_set(pattern, i))

        for i in range(M):
            cnt = 0
            for s in S[i]:
                cnt += switch[s]
            if cnt % 2 != P[i]:
                break
        else:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
