class Rmq:
    # 平方分割
    # 値を変更すると元のリストの値も書き換わる
    def __init__(self, a, sqrt_n=500):
        from itertools import zip_longest
        self.n = len(a)
        self.sqrt_n = sqrt_n
        self.layer1 = a
        self.layer0 = [min(values) for values in zip_longest(*[iter(a)]*sqrt_n, fillvalue=float("inf"))]

    def get_min(self, l, r):
        sqrt_n = self.sqrt_n
        parent_l, parent_r = l//sqrt_n+1, (r+1)//sqrt_n
        if parent_l < parent_r:
            return min(min(self.layer0[parent_l:parent_r]),
                       min(self.layer1[l:parent_l*sqrt_n]),
                       min(self.layer1[parent_r*sqrt_n:r]))
        else:
            return min(self.layer1[l:r])

    def set_value(self, idx, val):
        self.layer1[idx] = val
        idx //= self.sqrt_n
        self.layer0[idx] = min(self.layer0[idx], val)

    def chmin(self, idx, val):
        if self.layer1[idx] > val:
            self.set_value(idx, val)

    def debug(self):
        print("layer0=", self.layer0)
        print("layer1=", self.layer1)

    def __getitem__(self, item):
        return self.layer1[item]

    def __setitem__(self, key, value):
        self.set_value(key, value)


from operator import itemgetter
import sys

def main():
    N, M = map(int, input().split())
    LRC = list(zip(*[iter(map(int, sys.stdin.read().split()))]*3))
    LRC.sort(key=itemgetter(0))
    idx_LRC = 0
    inf = 1 << 60

    rmq = Rmq([inf] * (N+1))
    rmq.set_value(1, 0)
    for v in range(1, N+1):
        d = rmq.get_min(v, N+1)
        while idx_LRC < M:
            l, r, c = LRC[idx_LRC]
            if l <= v:
                rmq.chmin(r, d+c)
                idx_LRC += 1
            else:
                break
    ans = rmq[N]
    print(ans if ans < inf else -1)

main()
