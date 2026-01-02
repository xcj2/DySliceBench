import sys

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

    def update(self, i, x):
        i += self.len
        while i > 0:
            self.array[i] = max(self.array[i], x)
            i >>= 1
        # print(self.array)

    def get(self, i):
        return self.array[i + self.len]

    def get_maximum(self, l, r):
        L = l+self.len
        R = r+self.len
        ANS = -1 << 30

        while L < R:
            if L & 1:
                ANS = max(ANS, self.array[L])
                L += 1

            if R & 1:
                R -= 1
                ANS = max(ANS, self.array[R])
            L >>= 1
            R >>= 1

        return ANS


N = ni()
h_array = na()
a_array = na()

ans = SegmentTreeRMQ(N+1, 0)



for h, a in zip(h_array, a_array):
    tmp = ans.get_maximum(0, h) + a
    if ans.get(h) < tmp:
        ans.update(h, tmp)

print(ans.get_maximum(0, N+1))
