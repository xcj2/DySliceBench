#!/usr/bin/env python3
import sys
# from collections import Counter
INF = float("inf")


class MaxBit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s = max(s, self.tree[i])
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] = max(self.tree[i], x)
            i += i & -i


class MinBit:
    def __init__(self, n):
        self.size = n
        self.tree = [n-1] * (n + 1)

    def sum(self, i):
        s = self.size-1
        while i > 0:
            s = min(s, self.tree[i])
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] = min(self.tree[i], x)
            i += i & -i


def solve(N: int, P: "List[int]"):

    prev = MaxBit(N+2)
    foll = MinBit(N+2)
    seq = [0]*(N+2)

    inv = {p: i for i, p in enumerate(P)}
    # print(inv)
    # c = Counter()

    ans = 0
    for i in range(N, 0, -1):
        prev.add(inv[i]+2, inv[i]+1)
        foll.add(N-inv[i]+1, inv[i]+1)
        seq[inv[i]+1] = i

        # print("")
        # print("{}番目に{}を追加".format(inv[i]+1, i))
        # print("seq : ", seq)
        # print("prev: ", [prev.sum(j) for j in range(N+2)])
        # print("foll: ", [foll.sum(j) for j in range(N+2)][::-1])
        p = prev.sum(inv[i]+1)
        pp = prev.sum(p)
        f = foll.sum(N-inv[i])
        ff = foll.sum(N-f+1)
        # 前の数字との組み合わせ
        if p > 0:
            # (前、今) 前に伸ばす * 後ろに伸ばす
            ans += i*(p-pp)*(f-(inv[i]+1))
            # print("+ (A): ", i*(p-pp)*(f-(inv[i]+1)))
            # c[i] += (p - pp) * (f - (inv[i]+1))
        # 後ろの数字との組み合わせ
        if f < N+1:
            # (今、後) 前に伸ばす * 後に伸ばす
            ans += i*(inv[i]+1 - p) * (ff - f)
            # print("+ (B): ", i*(inv[i]+1 - p)*(ff-f))
            # c[i] += (ff - f) * ((inv[i]+1) - p)
    print(ans)
    # print([(i+1, c[i+1]) for i in range(N)])

    # guchoku = Counter()
    # for i in range(N):
    #     for j in range(i+1, N):
    #         guchoku[sorted(P[i:j+1])[-2]] += 1
    #         print(sorted(P[i:j+1])[-2], P[i:j+1])
    # print([(i+1, guchoku[i+1]) for i in range(N)])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P)


if __name__ == '__main__':
    main()
