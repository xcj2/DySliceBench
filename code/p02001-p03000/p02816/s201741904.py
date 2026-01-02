#!/usr/bin/env python3
import sys
INF = float("inf")


B = 10**7+7
MOD = 10**9+7


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
    return [i-N-1 for i in range(len(conc)) if Z[i] == N]


def solve(N: int, a: "List[int]", b: "List[int]"):

    c = [a[i] ^ a[(i+1) % N]for i in range(N)]
    d = [b[i] ^ b[(i+1) % N]for i in range(N)]*2
    i = -1
    k_cand = zfindall(d, c, separator=[-1])
    # print(k_cand)

    ans = []
    if len(k_cand) == 0:
        return
    if k_cand[0] % N == 0:
        print(0, b[0] ^ a[0])
        for k in k_cand[:0:-1]:
            if k < N:
                print(-k % N, b[0] ^ a[-k % N])
    else:
        for k in k_cand[::-1]:
            if k < N:
                print(-k % N, b[0] ^ a[-k % N])
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
