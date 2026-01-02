def cumsum(T, K):
    R = [[0] * K for _ in range(K)]
    for i in range(K):
        t = 0
        for j in range(K):
            t += T[i][j]
            R[i][j] = t
    for i in range(K):
        t = 0
        for j in range(K):
            t += R[j][i]
            R[j][i] = t
    return R

def fm(B, W, K):
    m = 0
    for i in range(K):
        for j in range(K):
            t = B[i][j]
            if i == K - 1 or j == K - 1:
                t += W[K - 1][K - 1] - W[i][j]
            else:
                t += B[K - 1][K - 1] - B[K - 1][j] - B[i][K - 1] + B[i][j]
                t += W[K - 1][j] + W[i][K - 1] - 2 * W[i][j]
            m = max(m, t)
    return m

def main():
    N, K = map(int, input().split())
    K2 = 2 * K
    B = [[0] * K for _ in range(K)]
    W = [[0] * K for _ in range(K)]
    for _ in range(N):
        x1, y1, c = input().split()
        x, y = int(x1) % K2, int(y1) % K2
        if c == 'B':
            x = (x - K) % K2
        if x >= K and y >= K:
            x, y = x - K, y - K
        if x < K and y < K:
            B[x][y] += 1
        else:
            x, y = (x - K, y) if y < K else (x, y - K)
            W[x][y] += 1
    B = cumsum(B, K)
    W = cumsum(W, K)
    return max(fm(B, W, K), fm(W, B, K))

print(main())
