import sys
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


class SegmentTreeRMQ(object):  # 1-indexed [l,r)
    def __init__(self, size, value):
        self.len = 1 << size.bit_length()
        # print(self.len)
        self.array = [value] * (2 * self.len)

    def update(self, i, x):  # 0-indexed
        i += self.len
        while i > 0:
            self.array[i] = min(self.array[i], x)
            i >>= 1
        # print(self.array)

    def get(self, i):  # 0-indexed
        return self.array[i + self.len]

    def get_minimum(self, l, r):  # 0-indexed
        L = l+self.len
        R = r+self.len
        ANS = 1 << 30

        while L < R:
            if L & 1:
                ANS = min(ANS, self.array[L])
                L += 1

            if R & 1:
                R -= 1
                ANS = min(ANS, self.array[R])
            L >>= 1
            R >>= 1

        return ANS


N, K = na()
P = na()

if N == K or N == 2:
    print(1)
    exit()


min_tree = SegmentTreeRMQ(N, N)
max_tree = SegmentTreeRMQ(N, 1)

for i, p in enumerate(P):
    min_tree.update(i, p)
    max_tree.update(i, -p)

no_change = [0] * (N-K+1)

last = -1

for i in range(N):
    if i - last >= K:
        no_change[i-K+1] = 1
    if i == N-1:
        break
    if P[i] > P[i+1]:
        last = i

# print(no_change)


ans = 1
no_count = 0

for i in range(N-K):
    if P[i] > min_tree.get_minimum(i+1, i+K+1) or -P[i+K] > max_tree.get_minimum(i+1, i+K+1):
        ans += 1
        if no_change[i] == 1:
            no_count += 1
    if i == (N-K-1) and no_change[N-K] == 1:
        no_count += 1

print(ans - max(0, no_count-1))
