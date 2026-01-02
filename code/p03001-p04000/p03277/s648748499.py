from itertools import accumulate


class Bit:
    # 参考1: http://hos.ac/slides/20140319_bit.pdf
    # 参考2: https://atcoder.jp/contests/arc046/submissions/6264201
    # 検証: https://atcoder.jp/contests/arc046/submissions/7435621
    # values の 0 番目は使わない
    # len(values) を 2 冪 +1 にすることで二分探索の条件を減らす
    def __init__(self, a):
        if hasattr(a, "__iter__"):
            le = len(a)
            self.n = 1 << le.bit_length()  # le を超える最小の 2 冪
            self.values = values = [0] * (self.n + 1)
            values[1:le + 1] = a[:]
            for i in range(1, self.n):
                values[i + (i & -i)] += values[i]
        elif isinstance(a, int):
            self.n = 1 << a.bit_length()
            self.values = [0] * (self.n + 1)
        else:
            raise TypeError

    def add(self, i, val):
        n, values = self.n, self.values
        while i <= n:
            values[i] += val
            i += i & -i

    def sum(self, i):  # (0, i]
        values = self.values
        res = 0
        while i > 0:
            res += values[i]
            i -= i & -i
        return res

    def bisect_left(self, v):  # self.sum(i) が v 以上になる最小の i
        n, values = self.n, self.values
        if v > values[n]:
            return None
        i, step = 0, n >> 1
        while step:
            if values[i + step] < v:
                i += step
                v -= values[i]
            step >>= 1
        return i + 1

def solve(M, N, A):
    A_sign = [-1 if a <= M else 1 for a in A]
    A_sign_cum = list(accumulate(A_sign))
    geta = N + 2
    bit = Bit(2*N + 4)
    bit.add(geta, 1)
    cnt = 0  # 中央値が M 以下になる区間の個数
    #if True:
    #    print(M, A_sign, A_sign_cum)
    for i, a in enumerate(A_sign_cum, 1):
        cnt += i - bit.sum(geta + a)
        #print(cnt, end=" ")
        bit.add(geta + a, 1)
    #print()
    #print(N * (N+1) // 4 + 1, cnt)
    return N * (N+1) // 4 + 1 <= cnt


def main():
    N = int(input())
    A = list(map(int, input().split()))

    # cnt = 0
    # for i in range(N):
    #     for j in range(i+1, N+1):
    #         if sorted(A[i:j])[(j-i)//2] <= 5:
    #             cnt += 1
    #             print(i, j)
    # print(cnt)

    A_sorted = sorted(A)
    ng, ok = -1, N-1
    while ng + 1 < ok:
        c = (ng + ok) // 2
        M = A_sorted[c]
        if solve(M, N, A):
            ok = c
        else:
            ng = c
    print(A_sorted[ok])

main()
