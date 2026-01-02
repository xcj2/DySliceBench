class Bit:
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

    # i+1番目からR番目まで足すとt以上となるような最小のRを返す
    def bisect_plus(self, i, t):
        L = i
        R = self.size
        R_prev = R
        sum_i = self.sum(i)
        while True:
            range_sum = self.sum(R) - sum_i
            if range_sum < t:
                if R == self.size:
                    return self.size + 1
                L, R = R, R_prev
            else:
                R_prev = R
                R = (L + R + 1) // 2
                if R == R_prev:
                    return R

    # L番目からi-1番目まで足すとt以上となるような最小のLを返す
    def bisect_minus(self, i, t):
        L = 1
        R = i
        L_prev = L
        sum_i = self.sum(i - 1)
        while True:
            range_sum = sum_i - self.sum(L - 1)
            if range_sum < t:
                if L == 1:
                    return 0
                L, R = L_prev, L
            else:
                L_prev = L
                L = (L + R) // 2
                if L == L_prev:
                    return L


N = int(input())
S_raw = list(map(int, input().split()))

S_raw.sort()
k = 1
S = [1]
for i in range(1, len(S_raw)):
    if S_raw[i] != S_raw[i-1]:
        k += 1
    S.append(k)

bit = Bit(S[-1] + 1)
for s in S:
    bit.add(s, 1)
slimes = [S[-1]]
for t in range(N):
    slimes_new = []
    for sl in slimes:
        sl_new = bit.bisect_minus(sl, 1)
        if sl_new == 0:
            print('No')
            exit()
        slimes_new.append(sl_new)
        bit.add(sl_new, -1)
    slimes.extend(slimes_new)

print('Yes')
