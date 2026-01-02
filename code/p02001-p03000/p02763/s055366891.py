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
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = [dic[s] for s in input().rstrip()]
    Q = int(input())
    Query = [[i for i in input().split()] for _ in [0]*Q]
    BIT26 = [RangeUpdate(N) for _ in [0]*26]
    for i, j in enumerate(S, start=1):
        BIT26[j].add(i, i, 1)
    answer = []
    for A in Query:
        if A[0] == "1":
            i = int(A[1])
            j = S[i-1]
            BIT26[j].add(i, i, -1)
            j = dic[A[2]]
            S[i-1] = j
            BIT26[j].add(i, i, 1)
        else:
            le = int(A[1])
            ri = int(A[2])
            ans = 0
            cur = 0
            for i in range(26):
                v = BIT26[i].sum(le, ri)
                if 0 < v:
                    ans += 1
                cur += v
                if ri - le + 1 == v:
                    break
            answer.append(ans)
    print(*answer, sep="\n")


if __name__ == '__main__':
    main()
