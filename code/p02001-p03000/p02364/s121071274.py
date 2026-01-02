# 最小全域木（Kraskal法　＋　UnionFind）
class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * (n)
        # print(self.rank)

    # 検索
    def findSet(self, x):
        # 根ならその番号を返す
        if self.par[x] == x:
            return x
        else:
            # 根でないなら、親の要素で再走査
            # 走査する過程で親を書き換える(根を親につなぎなおす)
            self.par[x] = self.findSet(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        # 根を探す
        x = self.findSet(x)
        y = self.findSet(y)
        # 木の高さを比較し,高いほうに低いほうをくっつける
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            # 木の高さが同じなら片方の木の高さを1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.findSet(x) == self.findSet(y)


# Kruskal法により最小全域木を求める
def compute_mst_kruskal(v, edges):
    # 重みの昇順で辺(edge)を並べ替える（あとで重みが最小のものから順番に走査するので）
    #重み(x[2])をkeyにしてソート
    edges = sorted(edges,key=lambda x: x[2])
    # | V |でUnionFind作成
    uf = UnionFind(v)
    mst = []

    # edgesが空になるまで繰り返す
    """
    for edge in edges:
        # ふたつの頂点が同じ木（集合）に属していないなら二つの木を連結する
        if not uf.in_the_same_set(edge.start, edge.end):
            uf.unite(edge.start, edge.end)
            mst.append(edge)
    return mst
    """
    i = 0
    # 重みが小さい順に辺を走査していく
    while i < len(edges):
        # 最小の辺を選択
        edge = edges[i]

        """
        start : 選択された辺の始点
        end   : 選択された辺の終点
        無向グラフなのでstart,end自体に大きな意味はない
        """
        start = edges[i][0]
        end   = edges[i][1]

        # start,endが同じ木に属していなかったら
        if not uf.same_check(start, end):
            #print(edge)
            uf.union(start,end)
            mst.append(edge)
        i = i + 1
    return mst

def buble_sort(tdlist):
    i=0
    while i < len(tdlist)-1:
        if tdlist[i][2] > tdlist[i+1][2]:
            tmp = tdlist[i]
            tdlist[i] = tdlist[i+1]
            tdlist[i+1] = tmp
            i = -1
        i = i + 1

    #print(tdlist)
    return tdlist


def main():
    #print()
    p = []  ##appendのために宣言が必要
    v, e = map(int, input().split())
    # v：頂点数
    # e：辺
    # 入力受付
    i = 0
    while i < e:
        try:
            p.append(list(map(int, input().split())))
            i = i + 1
        except:
            break;

    mst = compute_mst_kruskal(v, p)
    #print(sum(e.weight for e in mst))


    i = 0
    total_weight = 0
    while i < len(mst):
        total_weight = total_weight + mst[i][2]
        i = i + 1
    print(total_weight)



if __name__ == '__main__':
    main()
