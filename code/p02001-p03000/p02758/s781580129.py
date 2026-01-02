import bisect
import sys


sys.setrecursionlimit(10**6)
INF = 10**6


class SegTree:

    def __init__(self, N):
        self.N = N
        self.data = [- INF] * (2 * N - 1)

    def update(self, i, x):
        n = self.N + i - 1
        self.data[n] = x
        while n > 0:
            n = (n - 1) // 2
            self.data[n] = max(self.data[2 * n + 1], self.data[2 * n + 2])        

    def elem(self, i):
        return self.data[self.N + i - 1]

    def _query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return - INF
        if a <= l and r <= b:
            return self.data[k]
        val_left = self._query(a, b, 2 * k + 1, l, (l + r) // 2)
        val_right = self._query(a, b, 2 * k + 2, (l + r) // 2, r)
        return max(val_left, val_right)

    def query(self, a, b):
        return self._query(a, b, 0, 0, self.N)


def main():
    MOD = 998244353
    N = int(input())
    robot_list = [list(map(int, input().split())) for _ in range(N)]
    robot_list.sort()  # x座標の昇順でソート
    X = [robot[0] for robot in robot_list]
    D = [robot[1] for robot in robot_list]

    PW_N = 1
    while PW_N < N:
        PW_N *= 2
    next_robot_tree = SegTree(PW_N)
    next_robot_tree.update(N - 1, N)
    for n in range(N - 2, - 1, - 1):
        if X[n] + D[n] <= X[n + 1]:
            next_robot_tree.update(n, n + 1)
        else:
            next_robot = bisect.bisect_left(X, X[n] + D[n])
            next_robot = next_robot_tree.query(n, next_robot)
            next_robot_tree.update(n, next_robot)

    cnt = [0] * (N + 1)
    cnt[0] = 1
    for n in range(N):
        cnt[n + 1] += cnt[n]
        cnt[n + 1] %= MOD
        next_robot = next_robot_tree.elem(n)
        cnt[next_robot] += cnt[n]
        cnt[next_robot] %= MOD
    print(cnt[N])


if __name__ == '__main__':
    main()