N = int(input())
a = [int(x) for x in input().split()]

b = sorted(a)
M = ((N + 1) * N // 2 + 1) // 2


class BIT(object):
    def __init__(self, N=1):
        self.N = N
        self.bit = [0] * (N + 1)

    def add(self, i, x):
        while i <= self.N:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


def is_OK(x):
    S = [1] * N
    for i in range(N):
        if a[i] < x:
            S[i] = -1
        if i > 0:
            S[i] += S[i - 1]
    S = [0] + S
    min_S = min(S)
    max_S = max(S)

    bit = BIT(max_S - min_S + 1)
    cnt = 0
    for S_i in S:
        S_i = S_i - min_S + 1
        cnt += bit.sum(S_i)
        bit.add(S_i, 1)
    return cnt >= M


left, right = 0, 10 ** 9 + 1
while right - left > 1:
    mid = (left + right) // 2
    if is_OK(mid):
        left = mid
    else:
        right = mid

print(left)