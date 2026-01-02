import sys

read = sys.stdin.read
readline = sys.stdin.readline


class UnionFind():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1] * (n + 1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rnk = [0] * (n + 1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # すでに同じ木に属していた場合
        if x == y:
            return
        # 違う木に属していた場合rnkを見てくっつける方を決める
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return -self.root[self.Find_Root(x)]


N, M, K, *ABCD = map(int, read().split())
AB = ABCD[:M * 2]
CD = ABCD[M * 2:]
F = UnionFind(N)
friend = [[] for _ in range(N + 1)]
for A, B in zip(*[iter(AB)] * 2):
    F.Unite(A, B)
    friend[A].append(B)
    friend[B].append(A)

block = [[] for _ in range(N + 1)]
for C, D in zip(*[iter(CD)] * 2):
    block[C].append(D)
    block[D].append(C)

answer = []
for i in range(1, N + 1):
    cnt = F.Count(i) - 1
    for j in block[i]:
        if F.isSameGroup(i, j):
            cnt -= 1
    for j in friend[i]:
        if F.isSameGroup(i, j):
            cnt -= 1
    answer.append(cnt)

print(' '.join(map(str, answer)))
