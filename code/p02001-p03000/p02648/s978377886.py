import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


def merge(a, b):
    res = []
    i, j = 0, 0
    while i < len(a) or j < len(b):
        if j >= len(b) or (i < len(a) and a[i][0] < b[j][0]):
            w, v = a[i]
            i += 1
        else:
            w, v = b[j]
            j += 1
        if not res or res[-1][1] < v:
            res.append((w, v))
        elif res[-1][0] == w and res[-1][1] <= v:
            res.pop()
            res.append((w, v))
    return res


def best(L, a, b):
    res = 0
    i = 0
    j = len(b) - 1
    while i < len(a):
        w, v = a[i]
        if j < 0:
            break
        if b[j][0] + w > L:
            j -= 1
            continue
        res = max(res, v + b[j][1])
        i += 1
    return res


def main():
    N = int(input())
    VW = [(-1, -1)] + [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    query = tuple(tuple(map(int, input().split())) for _ in range(Q))

    dp = [[] for _ in range(2048)]
    dp[0] = [(0, 0)]
    for i in range(1, min(N + 1, 2048)):
        vi, wi = VW[i]
        a1 = dp[i // 2]
        a2 = [(w + wi, v + vi) for w, v in a1]
        dp[i] = merge(a1, a2)

    for n, L in query:
        a = [(0, 0)]
        while n >= 2048:
            vi, wi = VW[n]
            b = [(w + wi, v + vi) for w, v in a]
            a = merge(a, b)
            n //= 2
        print(best(L, a, dp[n]))


if __name__ == "__main__":
    main()