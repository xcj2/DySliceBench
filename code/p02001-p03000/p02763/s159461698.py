import sys
input = sys.stdin.readline


class SegTree():
    # ここでは操作の都合上根元のindexを1とする
    def __init__(self, lists, function, basement):
        self.n = len(lists)
        self.K = (self.n-1).bit_length()
        self.f = function
        self.b = basement
        self.seg = [basement]*2**(self.K+1)
        X = 2**self.K
        for i, v in enumerate(lists):
            self.seg[i+X] = v
        for i in range(X-1, 0, -1):
            self.seg[i] = self.f(self.seg[i << 1], self.seg[i << 1 | 1])

    def update(self, k, value):
        X = 2**self.K
        k += X
        self.seg[k] = value
        while k:
            k = k >> 1
            self.seg[k] = self.f(self.seg[k << 1], self.seg[(k << 1) | 1])

    def query(self, L, R):
        num = 2**self.K
        L += num
        R += num
        vL = self.b
        vR = self.b
        while L < R:
            if L & 1:
                vL = self.f(vL, self.seg[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.f(self.seg[R], vR)
            L >>= 1
            R >>= 1
        return self.f(vL, vR)


def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    que = [tuple(input().split()) for i in range(Q)]
    alpha = "abcdefghijklmnopqrstuvwxyz"
    Data = {alpha[i]: [0]*N for i in range(26)}
    for i in range(N):
        Data[S[i]][i] += 1
    SEG = {alpha[i]: SegTree(Data[alpha[i]], max, 0) for i in range(26)}
    for X, u, v in que:
        if X == "1":
            u = int(u)-1
            NOW = S[u]
            S[u] = v
            SEG[NOW].update(u, 0)
            SEG[v].update(u, 1)
        else:
            u, v = int(u)-1, int(v)-1
            res = 0
            for j in range(26):
                res += SEG[alpha[j]].query(u, v+1)
            print(res)


if __name__ == "__main__":
    main()