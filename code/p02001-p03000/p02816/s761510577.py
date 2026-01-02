#!/usr/bin/env python3
import sys
INF = float("inf")


B = 10**7+7
MOD = 10**9+7

# https://tjkendev.github.io/procon-library/python/string/rolling_hash.html


class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + s[i]) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod


def z_algorithm(S):
    """Zアルゴリズム
    https://snuke.hatenablog.com/entry/2014/12/03/214243 の二番目のコード
    """
    N = len(S)
    Z = [0]*N

    c = 0
    for i in range(1, N):
        if i+Z[i-c] < c+Z[c]:
            Z[i] = Z[i-c]
        else:
            j = max(0, c+Z[c]-i)
            while i+j < N and S[j] == S[i+j]:
                j += 1
            Z[i] = j
            c = i
    Z[0] = len(S)
    return Z


def zfindall(text, pattern, separator="$"):
    """テキストからパターンと一致する部分文字列を探す。
    開始インデックスを返す
    Zアルゴリズムを利用する
    """
    N = len(pattern)
    conc = pattern+separator+text
    Z = z_algorithm(conc)
    return {i-N-1 for i in range(len(conc)) if Z[i] == N}


def solve(N: int, a: "List[int]", b: "List[int]"):

    c = [a[i] ^ a[(i+1) % N]for i in range(N)]
    d = [b[i] ^ b[(i+1) % N]for i in range(N)]*2
    i = -1
    a1 = [0]*N
    a2 = [0]*N
    b1 = [0]*(2*N)
    k_cand = [True]*N
    for keta in range(30):
        mask = 1 << keta
        for i, aa in enumerate(a):
            a1[i] = (aa & mask) >> keta
            a2[i] = (~aa & mask) >> keta
        for i, bb in enumerate(b):
            b1[i] = (bb & mask) >> keta
            b1[i+N] = (bb & mask) >> keta
        P = RollingHash(a1, 97, MOD)
        Q = RollingHash(a2, 97, MOD)
        R = RollingHash(b1, 97, MOD)
        for i in range(N):
            if k_cand[i]:
                if not ((P.get(0, N) == R.get(i, i+N)) or
                        (Q.get(0, N) == R.get(i, i+N))):
                    k_cand[i] = False
        # k_cand1 = zfindall(b1, a1, separator=[-1])
        # k_cand2 = zfindall(b1, a2, separator=[-1])
        # for i in range(N):
        #     k_cand[i] = k_cand[i] & ((i in k_cand1) or (i in k_cand2))

    ans = []
    if len(k_cand) == 0:
        return
    if k_cand[0] == True:
        print(0, b[0] ^ a[0])
        for i, k in enumerate(k_cand[:0:-1], start=1):
            if k:
                print(i, b[0] ^ a[i])
    else:
        for i, k in enumerate(k_cand[::-1], start=1):
            if k:
                print(i, b[0] ^ a[i])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N - 1 - 0 + 1)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(N - 1 - 0 + 1)]  # type: "List[int]"
    solve(N, a, b)


if __name__ == '__main__':
    main()
