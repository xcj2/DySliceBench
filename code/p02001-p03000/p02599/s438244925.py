import sys
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


class SegmentTreeSUM(object):  # 1-indexed [l,r)
    def __init__(self, size):
        self.len = 1 << (size-1).bit_length()
        # print(self.len)
        self.array = [0 for _ in range(2 * self.len)]

    def update(self, i, x):  # 0-indexed
        i += self.len
        while i > 0:
            self.array[i] = self.array[i] + x
            i >>= 1
        # print(self.array)

    def get(self, i):  # 0-indexed
        return self.array[i + self.len]

    def get_sum(self, l, r):  # 0-indexed
        L = l+self.len
        R = r+self.len
        ANS = 0

        while L < R:
            if L & 1:
                ANS = ANS + self.array[L]
                L += 1

            if R & 1:
                R -= 1
                ANS = ANS + self.array[R]
            L >>= 1
            R >>= 1

        return ANS


N, Q = na()
c_array = na()

tree = SegmentTreeSUM(N)


q_array = []
for i in range(Q):
    l, r = na()
    q_array.append([i, l-1, r])

q_array = sorted(q_array, key=lambda x: x[2])
ans = [0] * Q
last_idx = [-1] * (N+1)
q_idx = 0
for i, c in enumerate(c_array):
    tree.update(i, 1)
    if last_idx[c] != -1:
        tree.update(last_idx[c], -1)
    last_idx[c] = i
    while(q_idx < Q and q_array[q_idx][2] == (i+1)):
        idx, l, r = q_array[q_idx]
        ans[idx] = tree.get_sum(l, r)
        q_idx += 1


print("\n".join(map(str, ans)))
