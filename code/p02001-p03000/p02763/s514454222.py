class Bit():
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


def enc(a):
    return ord(a) - ord('a')


N = int(input())
S = input()
bits = [Bit(N) for i in range(26)]

for i, s in enumerate(S):
    bits[enc(s)].add(i + 1, 1)


for _ in range(int(input())):
    t, l, r = input().split(" ")
    if t == '1':
        i = int(l)
        before = -1
        for before in range(26):
            if bits[before].sum(i) - bits[before].sum(i - 1) == 1:
                break
        after = enc(r)
        bits[before].add(i, -1)
        bits[after].add(i, 1)
    else:
        l, r = map(int, [l, r])
        ans = 0
        for c in range(26):
            if bits[c].sum(r) - bits[c].sum(l - 1) > 0:
                ans += 1
        print(ans)