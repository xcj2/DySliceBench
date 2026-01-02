from itertools import accumulate


class CoeffTable:
    def __init__(self, n):
        self.n = n
        if n == 2:
            (self.p2, self.p1, self.m1, self.m2) = (0, 1, 1, 0)
        if n % 2 == 0:
            self.p1 = self.m1 = 1
            self.p2 = self.m2 = (n - 1) // 2
        else:
            self.p1 = 0
            self.m1 = 2
            self.p2 = (n - 1) // 2
            self.m2 = (n - 2) // 2

    def reverse(self):
        (self.p2, self.p1, self.m1, self.m2) = (
            self.m2,
            self.m1,
            self.p1,
            self.p2,
        )

    def cumsum(self):
        return list(accumulate([self.p2, self.p1, self.m1, self.m2]))



def main(n, seq):
    seq = sorted(seq, reverse=True)
    coeff = CoeffTable(n)
    cm = coeff.cumsum()
    ans1 = (
        2 * sum(seq[0 : cm[0]])
        + 1 * sum(seq[cm[0] : cm[1]])
        - 1 * sum(seq[cm[1] : cm[2]])
        - 2 * sum(seq[cm[2] : cm[3]])
    )
    coeff.reverse()
    rcm = coeff.cumsum()
    ans2 = (
        2 * sum(seq[0 : rcm[0]])
        + 1 * sum(seq[rcm[0] : rcm[1]])
        - 1 * sum(seq[rcm[1] : rcm[2]])
        - 2 * sum(seq[rcm[2] : rcm[3]])
    )
    ans = max(ans1, ans2)
    print(ans)
    return


if __name__ == "__main__":
    n = int(input())
    sample = []
    for _ in range(n):
        sample.append(int(input()))
    main(n, sample)
