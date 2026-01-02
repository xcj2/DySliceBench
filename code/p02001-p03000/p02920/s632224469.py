class BinaryIndexTree:  # 1-indexed
    def __init__(self, N):
        """
        INPUT
        N [int] -> 全部0で初期化
        N [list] -> そのまま初期化
        """
        if isinstance(N, int):
            self.N = N
            self.depth = N.bit_length()
            self.tree = [0] * (N + 1)
            self.elem = [0] * (N + 1)
        elif isinstance(N, list):
            self.N = len(N)
            self.depth = self.N.bit_length()
            self.tree = [0] + N
            self.elem = [0] + N
            self._init()
        else:
            raise "INVALID INPUT: input must be int or list"

    def _init(self):
        size = self.N
        for i in range(1, self.N):
            if i + (i & -i) > size:
                continue
            self.tree[i + (i & -i)] += self.tree[i]

    def add(self, i, x):
        self.elem[i] += x
        while i <= self.N:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def lower_bound(self, val):
        if val <= 0:
            return 0
        i = 0
        k = 1 << self.depth
        while k:
            if i + k <= self.N and self.tree[i + k] < val:
                val -= self.tree[i + k]
                i += k
            k >>= 1
        return i + 1


N = int(input())
A = list(map(int, input().split()))
atoi = {a: i+1 for i, a in enumerate(sorted(set(A)))}

bit = BinaryIndexTree(len(atoi) + 5)

for a in A:
    i = atoi[a]
    bit.add(i, 1)


slime = []

p = bit.lower_bound(1 << N)
slime.append(p)
bit.add(p, -1)

for _ in range(N):
    next_slime = []
    for s in slime:
        tot = bit.sum(s - 1)
        p = bit.lower_bound(tot)
        if p == 0:
            print("No")
            exit()
        next_slime.extend([s, p])
        bit.add(p, -1)
    slime = next_slime
print("Yes")