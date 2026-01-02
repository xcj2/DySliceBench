import sys
input = sys.stdin.buffer.readline


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

    # L番目からi-1番目まで足すとt以上となるような最小のRを返す
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


def main():
    N, Q = map(int, input().split())
    ev = []
    x_list = []
    for _ in range(N):
        s, t, x = map(int, input().split())
        ev.append([s-x, 1, x])
        ev.append([t-x, -1, x])
        x_list.append(x)
    for _ in range(Q):
        d = int(input())
        ev.append([d, 0, 0])
    ev.sort(key=lambda p: p[0])
    x_list.sort()
    x_idx = {}
    for i in range(1, N+1):
        x_idx[x_list[i-1]] = i

    bit = Bit(N)
    x_list.append(-1)
    for pos, flag, x in ev:
        if flag == 0:
            print(x_list[bit.bisect_plus(0, 1) - 1])
        else:
            idx = x_idx[x]
            bit.add(idx, flag)


if __name__ == '__main__':
    main()
