#!/usr/bin/env python3
import sys
INF = float("inf")


# https://tjkendev.github.io/procon-library/python/string/rolling_hash.html

base = 37
mod = 10**9 + 9
pw = None


def rolling_hash(s):
    l = len(s)
    h = [0]*(l + 1)
    v = 0
    for i in range(l):
        h[i+1] = v = (v * base + s[i]) % mod
    return h


def setup_pw(l):
    global pw
    pw = [1]*(l + 1)
    v = 1
    for i in range(l):
        pw[i+1] = v = v * base % mod


def get(h, l, r):
    return (h[r] - h[l] * pw[r-l]) % mod


def solve(N: int, a: "List[int]", b: "List[int]"):

    c = [a[i] ^ a[(i+1) % N]for i in range(N)]
    d = [b[i] ^ b[(i+1) % N]for i in range(N)]*2
    i = -1
    a1 = [0]*N
    a2 = [0]*N
    b1 = [0]*(2*N)
    k_cand = [True]*N
    setup_pw(2*N)
    # 周期性を考慮すべきだが、二週分をとっていないのは何で対応しているのか
    # 一致パターンと、真逆パターンがあるはずだが、どこで見ているのか
    for keta in range(30):
        mask = 1 << keta
        for i, aa in enumerate(a):
            a1[i] = (aa & mask) >> keta
            a2[i] = (~aa & mask) >> keta
        for i, bb in enumerate(b):
            b1[i] = (bb & mask) >> keta
            b1[i+N] = (bb & mask) >> keta
        P = rolling_hash(a1)
        Q = rolling_hash(a2)
        R = rolling_hash(b1)
        for i in range(N):
            if k_cand[i]:
                if not ((get(P, 0, N) == get(R, i, i+N)) or
                        (get(Q, 0, N) == get(R, i, i+N))):
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
