import sys
from collections import deque
input = sys.stdin.readline

class UnionFind(object):
    def __init__(self, N):
        # 初期状態を定義。ルートは -1から始まり、-X と負数でグループのサイズをもつ
        self.node = [-1] * N

    def root(self, x):
        if self.node[x] < 0:
            # それ自身がrootなら自分のポジションを返却
            return x
        else:
            # ルートを再帰で辿って、それぞれルートに直つなぎにする
            self.node[x] = self.root(self.node[x])
            # 自分がつながってるルートのポジションを返却
            return self.node[x]

    def size(self, x):
        # xが所属するグループのサイズを取得
        # サイズは負の数で管理されてるので、-1倍して返却
        return -self.node[self.root(x)]

    def connect(self, x, y):
        a = self.root(x)  # x のrootの位置
        b = self.root(y)  # y のrootの位置

        # もう同じグループなら何もしない
        if a == b:
            return

        # サイズが大きい方をaとして取り回す
        if self.size(a) < self.size(b):
            a, b = b, a

        # aのサイズをbのサイズを含む形に更新する（負数同士の足し算）
        self.node[a] += self.node[b]
        # bをaに連結する
        self.node[b] = a

        return

    def show_nodes(self):
        return self.node


def main():
    N, M, K = map(int, input().split())

    tree = UnionFind(N)

    friends = [ list(map(int, input().split())) for _ in range(M)]

    for A, B in friends:
        tree.connect(A-1, B-1)

    ans = [tree.size(x) - 1 for x in range(N)]

    for A, B in friends:
        if tree.root(A-1) == tree.root(B-1):
            ans[A-1] -= 1
            ans[B-1] -= 1

    for _ in range(K):
        C, D = map(int,input().split())
        if tree.root(C - 1) == tree.root(D - 1):
            ans[C-1] -= 1
            ans[D-1] -= 1

    print(*ans)


if __name__ == "__main__":
    main()
