def ii():
    return int(input())


def lii():
    return list(map(int, input().split(' ')))


def lvi(N):
    l = []
    for _ in range(N):
        l.append(ii())
    return l


def lv(N):
    l = []
    for _ in range(N):
        l.append(input())
    return l


def main():
    N, K = lii()
    a = lii()
    min_ix = None
    for i, v in enumerate(a):
        if v == 1:
            min_ix = i
            break

    def t(n, k):
        if n <= 0: return 0, 0

        ans = n // k
        if n % k:
            ans += 1
        return ans, n % k

    if N-1 - min_ix >= K-1 and min_ix >= K-1:
        ans1, p1 = t(min_ix, K-1)
        ans2, p2 = t(N-1 - min_ix, K-1)
        ans = ans1 + ans2
        if p1 > 0 and p2 > 0 and p1 + p2 <= K-1:
            ans -= 1
        return ans

    elif min_ix < K-1:
        d = K-1 - min_ix
        ans, _ = t(N-1 - min_ix - d, K-1)
        return 1 + ans

    elif N-1 - min_ix < K-1:
        d = K-1 - (N-1 - min_ix)
        ans, _ = t(min_ix - d, K-1)
        return ans + 1


if __name__ == '__main__':
    print(main())