C = [[0] * 2001 for _ in range(2001)]
C[0][0] = 1
for i in range(2000):
    for j in range(i + 1):
        C[i + 1][j] += C[i][j]
        C[i + 1][j + 1] += C[i][j]


def comb(n, k):
    return C[n][k]


def ff(n, k):
    return comb(n + k - 1, k - 1)


def f(n, k):
    if k > n:
        return 0
    if n == 0 and k == 0:
        return 1
    if 1 > k:
        return 0
    return ff(n - k, k)


def main():
    N, K = map(int, input().split())
    for i in range(1, K + 1):
        b = f(K, i)
        r = 0
        r += f(N - K, i - 1)
        r += f(N - K, i)
        r += f(N - K, i)
        r += f(N - K, i + 1)
        ans = b * r % 1000000007
        print(ans)


main()
