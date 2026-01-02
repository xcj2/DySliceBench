def main():
    import sys
    input = sys.stdin.readline

    N, a0, d, mod = map(int, input().split())

    def matmul(A, B):
        C = [[0] * len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
        return C

    def matpow(A, p):
        n = len(A)
        B = [[0] * n for _ in range(n)]
        for i in range(n):
            B[i][i] = 1
        while p > 0:
            if p & 1:
                B = matmul(B, A)
            A = matmul(A, A)
            p >>= 1
        return B

    ans = [[a0%mod], [a0%mod], [d%mod]]
    ok_prev = 0
    for i in range(len(str(a0)), 20):
        ok = N
        ng = -1
        mid = (ok+ng)//2
        while ok - ng > 1:
            if len(str(a0 + d * mid)) >= i+1:
                ok = mid
            else:
                ng = mid
            mid = (ok+ng)//2

        mat = [[(10**i)%mod, 1, 1],
               [0, 1, 1],
               [0, 0, 1]]
        ans = matmul(matpow(mat, ok - ok_prev-1), ans)
        ok_prev = ok-1
        if ok == N:
            break
    print(ans[0][0])


if __name__ == '__main__':
    main()
