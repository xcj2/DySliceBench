# ABC106D - AtCoder Express 2
def build_2dcum(A: "Array[Array[int]]") -> "Array[Array[int]]":
    from itertools import accumulate as acc

    return [list(acc(a)) for a in zip(*[acc(a) for a in A])]


def respond_2dcum(l: int, r: int, A: "Array[Array[int]]") -> int:
    return A[r][r] - A[l - 1][r] - A[r][l - 1] + A[l - 1][l - 1]


def main():
    # 2D cumulative sum (naive ver.)
    N, M, Q, *X = map(int, open(0).read().split())
    LR, PQ = X[: 2 * M], X[2 * M :]
    imos = [[0] * (N + 1) for _ in range(N + 1)]
    for l, r in zip(*[iter(LR)] * 2):
        imos[l][r] += 1
    imos = build_2dcum(imos)
    ans = []
    for p, q in zip(*[iter(PQ)] * 2):
        x = respond_2dcum(p, q, imos)
        ans.append(x)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()