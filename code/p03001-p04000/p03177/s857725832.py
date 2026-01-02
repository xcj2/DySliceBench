
def resolve():
    def mat_mul(a, b):
        H = len(a)
        W = len(b[0])
        K = len(a[0])

        C = [[0] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                for k in range(K):
                    C[i][j] += a[i][k] * b[k][j]
                    C[i][j] %= MOD
        return C

    def mat_pow(a, p):
        n = len(a)
        ret = [[0] * n for _ in range(n)]
        for i in range(n):
            ret[i][i] = 1

        while p > 0:
            if p % 2 == 1:
                ret = mat_mul(ret, a)
            a = mat_mul(a, a)
            p >>= 1
        return ret

    MOD = 10 ** 9 + 7
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    ret = mat_pow(AB, K)
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += ret[i][j]
            ans %= MOD

    print(ans)


if __name__ == "__main__":
    resolve()
