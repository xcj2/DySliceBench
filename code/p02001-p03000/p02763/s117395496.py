class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


class RangeUpdate:
    def __init__(self, n):
        self.p = BIT(n + 1)
        self.q = BIT(n + 1)

    def add(self, s, t, x):
        t += 1
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)

    def sum(self, s, t):
        t += 1
        return self.p.sum(t) + self.q.sum(t) * t - \
            self.p.sum(s) - self.q.sum(s) * s


def main():
    from string import ascii_lowercase
    dic = {s: i for i, s in enumerate(ascii_lowercase)}
    N = int(input())
    S = [s for s in input()]
    BIT26 = [RangeUpdate(N) for i in range(26)]
    for i, s in enumerate(S):
        j = dic[s]
        BIT26[j].add(i+1, i+1, 1)
    Q = int(input())
    for query in range(Q):
        A = [i for i in input().split()]
        if A[0] == "1":
            i = int(A[1])
            c = A[2]
            pre = S[i-1]
            j = dic[pre]
            BIT26[j].add(i, i, -1)
            S[i-1] = c
            j = dic[c]
            BIT26[j].add(i, i, 1)
        else:
            le = int(A[1])
            ri = int(A[2])
            ans = 0
            for i in range(26):
                if 0 < BIT26[i].sum(le, ri):
                    ans += 1
            print(ans)


if __name__ == '__main__':
    main()
