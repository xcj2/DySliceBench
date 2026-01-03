from bisect import bisect

def solve(N, A, B, H, total, M):
    class Solver:
        def __init__(self, N, A, B, H, total):
            self.N = N
            self.B = B
            self.BA = A-B
            self.H = H
            self.len = idiv(total, B)

        def __getitem__(self, k):
            Bk = self.B * k
            cnt = 0
            for i in range(self.N):
                h = H[i] - Bk
                if h < 0:
                    continue
                cnt += idiv(h, self.BA)
                if cnt > k:
                    return -1
            #print("[%d]"%k, cnt, k)
            return 1 if cnt <= k else -1

        def __len__(self):
            return self.len

    k0 = idiv(total, (B*N+A))
    s = Solver(N, A, B, H, total)
    k = bisect(s, 0, k0, idiv(M, B))
    print(k)

def main():
    input = open(0).readline
    N, A, B = map(int, input().split())
    H = [0]*N
    M = 0
    total = 0
    for i in range(N):
        h = int(input())
        H[i] = h
        M = max(M, h)
        total += h
    solve(N, A, B, H, total, M)

def idiv(x, y):
    if x <= 0:
        return 0
    q, r = divmod(x, y)
    return q + (1 if r > 0 else 0)



main()
