import sys
input = sys.stdin.readline

class SegmentTree:
    # リストからセグメントツリーを構成
    def __init__(self, list_, ide_ele=0):
        tmp = 1
        while tmp < len(list_):
            tmp *= 2
        self.n = tmp
        self.l = [ide_ele] * (2 * self.n - 1)
        self.ide_ele = ide_ele
        self.init_val(list_)

    def func(self, x, y):
        return min(x, y)

    def init_val(self, list_):
        # list_の値で葉を埋める
        for i, val in enumerate(list_):
            self.l[self.n - 1 + i] = val
        # 下の段から初期値を埋めていく
        for i in range(self.n-2, -1, -1):
            self.l[i] = self.func(self.l[i*2+1], self.l[i*2+2])
    
    # i番目をvalで更新
    def update(self, i, val):
        i = self.n - 1 + i
        self.l[i] = val
        while i > 0:
            i = (i-1) // 2
            self.l[i] = self.func(self.l[i*2+1], self.l[i*2+2])
    
    # [a, b)の最小値を返す. l, rはノードkに対応した区間
    def query(self, a, b, k, l, r):
        if r <= a or b <= l:# 存在しない区間を参照
            return self.ide_ele  # エラーを返す
        if a <= l and r <= b:# 区間を完全に含む
            return self.l[k]
        vl = self.query(a, b, k*2+1, l, (l+r)//2)
        vr = self.query(a, b, k*2+2, (l+r)//2, r)
        return self.func(vl, vr)

def main():
    N, Q = map(int, input().split())
    tmp = (1 << 31) - 1
    seg = SegmentTree([tmp] * N, ide_ele=tmp)

    # print("init")
    # print(seg.l)

    for i in range(Q):
        c, x, y = map(int, input().split())
        if c == 0:
            # print("update: l[{}]={} -> {}".format(x, seg.l[x], y))
            seg.update(x, y)
        else:
            # print("min: {}~{}".format(x, y))
            print(seg.query(x, y+1, 0, 0, seg.n))
        # print(seg.l)

if __name__ == "__main__":
    main()
