INF_MAX = 2 ** 31 - 1


class Segment_tree():
    def __init__(self, N):
        self.N = 1
        while self.N < N:
            # 完全二分木にするために2のべき乗にする
            self.N *= 2

        self.dat = []
        for i in range(2 * self.N - 1):
            # indexが0を頂点とするsegment_treeを作る
            self.dat.append(INF_MAX)

    def update(self, k, x):
        k += self.N - 1
        # 指定しているkにsegmenttreeのindexを合わせる
        self.dat[k] = x
        while k > 0:
            # datの下から更新して行く
            k = int((k - 1) / 2)
            self.dat[k] = min(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    def find(self, a, b, k, l, r):
        if r < a or b < l:
            # a,bが区間に存在しないとき
            return INF_MAX
        if a <= l and r <= b:
            # 区間a,bがl,rを完全に含んでいるとき
            return self.dat[k]
        else:
            mid = int((l + r) / 2)
            # 左の子と右の子にいく
            vl = Segment_tree.find(self, a, b, k * 2 + 1, l, mid)
            vr = Segment_tree.find(self, a, b, k * 2 + 2, mid + 1, r)
            return min(vl, vr)


def main():
    N, Q = map(int, input().split())
    segment_tree = Segment_tree(N)
    for i in range(Q):
        command, a, b = map(int, input().split())
        if command == 0:
            Segment_tree.update(segment_tree, a, b)
        else:
            if a > b:
                a, b = b, a
            min_number = Segment_tree.find(segment_tree, a, b, 0, 0, segment_tree.N - 1)
            print(min_number)


if __name__ == "__main__":
    main()

