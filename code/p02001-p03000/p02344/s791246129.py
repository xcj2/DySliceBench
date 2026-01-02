class WeightedUnionFindTree():
    '''ランク付きUnionFind木'''
    def __init__(self, n):
        ''' 初期化 '''
        self.par = list(range(n))#自分自信を根とする
        self.rank = [0] * n # 木の高さ 最初は0
        self.w = [0] * n # 重み

    def root(self, x):
        ''' 木の根を求める '''
        if self.par[x] == x:#自分が根ノードなら
            return x

        root = self.root(self.par[x])
        self.w[x] += self.w[self.par[x]]# 累積和をとる
        self.par[x] = root
        return root
    def relate(self, x, y, weight=0):
        # x と y の root へ (x と y が既につながっていたらreturn
        root_x, root_y = self.root(x), self.root(y)
        if root_x == root_y: return;
        #木の高さ-ランクが低い方に繋げる
        if self.rank[root_x] < self.rank[root_y]:
            self.par[root_x] = root_y # 低いroot_xにroot_yを繋げ、低い方が根なのでひく
            self.w[root_x] = weight - self.w[x] + self.w[y]
        else:
            self.par[root_y] = root_x # 逆
            self.w[root_y] = -weight + self.w[x] - self.w[y]
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

    def same(self, x, y):
        #xとyが同じ集合に属するか
        return self.root(x) == self.root(y)

    def diff(self, x, y):
        if self.same(x, y):
            return self.w[x] - self.w[y]
        else:
            return "?"

def querying(queries, uft):
    for query in queries:
        if query[0] == 0:#unite
            uft.relate(query[1], query[2], query[3])
        else:
            print(uft.diff(query[1], query[2]))

if __name__ == '__main__':
    # https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_1_B
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]
    uft = WeightedUnionFindTree(n)#instant UnionFindTree
    querying(queries, uft)#Querying

