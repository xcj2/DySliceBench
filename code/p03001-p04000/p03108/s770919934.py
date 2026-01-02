class UnionFind:
    def __init__(self, size):
        self.parent = [-1 for i in range(size)]#非負なら親ノード，負ならグループの要素数

    def root(self, x): #root(x): xの根ノードを返す．
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x]) #xをxの根に直接つなぐ
            return self.parent[x]

    def merge(self, x, y): #merge(x,y): xのいるグループと$y$のいるグループをまとめる
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]: #xの要素数がyの要素数より「小さい」とき入れ替える
            x,y=y,x
        self.parent[x] += self.parent[y] #xの要素数を更新
        self.parent[y] = x #yをxにつなぐ
        return True

    def issame(self, x, y): #same(x,y): xとyが同じグループにあるならTrue
        return self.root(x) == self.root(y)

    def size(self,x): #size(x): xのいるグループの要素数を返す
        return -self.parent[self.root(x)]

def solve():
    N, M = map(int, input().split())
    bridges = [[int(i) - 1 for i in input().split()] for i in range(M)]
    ans = [N * (N - 1) // 2]

    uf = UnionFind(N)
    for bridge in reversed(bridges):
        A, B = bridge
        if uf.issame(A, B):
            ans.append(ans[-1])
        else:
            ans.append(ans[-1] - uf.size(A) * uf.size(B))
            uf.merge(A, B)
    ans.pop(-1)
    return '\n'.join(map(str, reversed(ans)))

print(solve())
