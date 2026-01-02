# RMQ のパフォーマンステスト
class Rmq:
    # 平方分割
    # 値を変更すると元のリストの値も書き換わる
    # 検証: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3990681
    def __init__(self, a, sqrt_n=150, inf=(1<<31)-1):
        self.sqrt_n = sqrt_n
        if hasattr(a, "__iter__"):
            from itertools import zip_longest
            self.n = len(a)
            self.layer0 = [min(values) for values in zip_longest(*[iter(a)]*sqrt_n, fillvalue=inf)]
            self.layer1 = a
        elif isinstance(a, int):
            self.n = a
            self.layer0 = [inf] * ((a - 1) // sqrt_n + 1)
            self.layer1 = [inf] * a
        else:
            raise TypeError

    def get_min(self, l, r):
        sqrt_n = self.sqrt_n
        parent_l, parent_r = l//sqrt_n+1, (r-1)//sqrt_n
        if parent_l < parent_r:
            return min(min(self.layer0[parent_l:parent_r]),
                       min(self.layer1[l:parent_l*sqrt_n]),
                       min(self.layer1[parent_r*sqrt_n:r]))
        else:
            return min(self.layer1[l:r])

    def set_value(self, idx, val):
        self.layer1[idx] = val
        idx0 = idx // self.sqrt_n
        idx1 = idx0 * self.sqrt_n
        self.layer0[idx0] = min(self.layer1[idx1:idx1+self.sqrt_n])

    def chmin(self, idx, val):
        if self.layer1[idx] > val:
            self.layer1[idx] = val
            idx //= self.sqrt_n
            self.layer0[idx] = min(self.layer0[idx], val)

    def debug(self):
        print("layer0=", self.layer0)
        print("layer1=", self.layer1)

    def __getitem__(self, item):
        return self.layer1[item]

    def __setitem__(self, key, value):
        self.set_value(key, value)


from operator import itemgetter

N, M = map(int, input().split())
LRC = [list(map(int, input().split())) for _ in range(M)]
LRC.sort(key=itemgetter(0))

idx_LRC = 0
q = []

inf = 10**18
seg = Rmq(N+1, inf=inf)

seg.set_value(1, 0)
for v in range(1, N + 1):
    d = seg.get_min(v, N + 1)
    while idx_LRC < M:
        l, r, c = LRC[idx_LRC]
        if l <= v:
            seg.chmin(r, d+c)
            idx_LRC += 1
        else:
            break
ans = seg[N]
print(ans if ans != inf else -1)
