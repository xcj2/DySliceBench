class BinaryIndexTree:  # 1-indexed
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


def Alp(s):
    return ord(s)-ord("a")


if __name__ == "__main__":
    N = int(input())
    S = list(input())
    Q = int(input())

    bit = [BinaryIndexTree(N) for _ in range(26)]
    for i, s in enumerate(S, start=1):
        bit[Alp(s)].add(i, 1)

    ans = []
    for _ in range(Q):
        q = input().split()
        if q[0] == "1":
            i = int(q[1]) - 1
            c = q[2]

            bit[Alp(c)].add(i+1, 1)
            bit[Alp(S[i])].add(i+1, -1)
            S[i] = c
        else:
            l = int(q[1])
            r = int(q[2])
            tmp = 0
            for i in range(26):
                b = bit[i]
                if b.sum(r) - b.sum(l - 1) > 0:
                    tmp += 1
            ans.append(tmp)

    print(*ans, sep="\n")
