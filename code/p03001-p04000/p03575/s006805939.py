#-*-coding:utf-8-*-

class UnionFind:
    def __init__(self, n):
    # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.parent = [i for i in range(n + 1)]
    # 木の高さを格納する（初期状態では0）
        self.rank = [0] * (n + 1)
    #検索
    def find(self, x):
    #根ならその番号を返す
        if self.parent[x] == x:
            return x
        else:
    # 走査していく過程で親を書き換える
            self.parent[x] = self.find(self.parent[x])
            return self.find(self.parent[x])
    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
    #併合
    def unite(self, x, y):
    #根を探す
        x = self.find(x)
        y = self.find(y)
    # 木の高さを比較し、低いほうから高いほうに辺を張る
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
    # 木の高さが同じなら片方を1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

def main():

    n, m = map(int, input().split())
    es = []

    for _ in range(m):
        a, b = map(int, input().split())
        es.append((a, b))
        
    ans = 0
    for i in range(m):
        u = UnionFind(n)
        for j, e in enumerate(es):
            if j != i:
                a, b = e
                u.unite(a, b)
        a, b = es[i]
        if not u.same_check(a, b):
            ans += 1
    
    print(ans)
        
if __name__ == '__main__':
    main()