import sys
readline = sys.stdin.buffer.readline
import numpy as np
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, K = map(int, readline().split())
    A = list(list(map(int, readline().split())) for _ in range(N))
    A = np.array(A)
    def dot(A, B):
        C = np.zeros((N, N), np.int64)
        for n in range(N):
            C[n] = (A[n, :][:, None] * B % MOD).sum(axis=0) % MOD
        return C

    def matrix_power(A, n):
        if n == 0:
            return np.eye(N, dtype=np.int64)
        X = matrix_power(A, n // 2)
        X = dot(X, X)
        return dot(A, X) if n & 1 else X

    ans = matrix_power(A,K)
    print(ans.sum() %MOD)


if __name__ == '__main__':
    main()