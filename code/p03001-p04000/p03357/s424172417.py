def main():
    import sys
    input = sys.stdin.readline

    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i


    N = int(input())
    A = [0] * (2*N)
    idx_W = [0] * (N+1)
    idx_B = [0] * (N+1)
    for i in range(N*2):
        c, a = input().split()
        if c == 'B':
            A[i] = int(a)
            idx_B[A[i]] = i+1
        else:
            A[i] = -int(a)
            idx_W[-A[i]] = i + 1

    cost_W = [[0] * (N+2) for _ in range(N+1)]
    cost_B = [[0] * (N+2) for _ in range(N+1)]
    cost_W_imos = [0] * (N+1)
    cost_B_imos = [0] * (N+1)
    for i in range(2*N):
        if A[i] > 0:
            Ai = A[i]
            cost_W_imos[Ai] = 1
            for j in range(N, 0, -1):
                if j == N:
                    cost_B[Ai][j] = cost_B_imos[j]
                else:
                    cost_B[Ai][j] = cost_B[Ai][j+1] + cost_B_imos[j]
        else:
            Ai = -A[i]
            cost_B_imos[Ai] = 1
            for j in range(N, 0, -1):
                if j == N:
                    cost_W[Ai][j] = cost_W_imos[j]
                else:
                    cost_W[Ai][j] = cost_W[Ai][j + 1] + cost_W_imos[j]

    inv_W = [0] * (N+1)
    inv_B = [0] * (N+1)
    bit_W = Bit(2*N+1)
    bit_B = Bit(2*N+1)
    for i in range(N, 0, -1):
        inv_W[i] = bit_W.sum(idx_W[i])
        inv_B[i] = bit_B.sum(idx_B[i])
        bit_W.add(idx_W[i], 1)
        bit_B.add(idx_B[i], 1)

    inf = (N*2)**2
    dp = [[inf] * (N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N+1):
        for j in range(N+1):
            if i+1 <= N:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + cost_W[i+1][j+1] + inv_W[i+1])
            if j+1 <= N:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + cost_B[j + 1][i + 1] + inv_B[j + 1])
    print(dp[N][N])


if __name__ == '__main__':
    main()
