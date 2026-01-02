#Union Find

class UnionFind:
    """
    par  : 木の親要素を管理par[x]==xのときそのノードは根,
            初期状態例:[0,1,2,3]それぞれが親
                        [0,0]のとき0が根で1の親は0であることを示す
    rank : 木の高さを格納,併合する際に木の高さが高いものに低いものをくっつける形になるから

    """
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * (n)
        #print(self.rank)

    """
    引数のノードの根を検索
    再起関数で親の親の親の...という形で根にたどり着くまで繰り返す
    """
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
        #根を探す
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


    """
    同じ集合に属するか判定＝二つの要素の根が同じかどうか判定
    """
    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.findSet(x) == self.findSet(y)


def main():
    p = []  ##appendのために宣言が必要
    n, q = map(int, input().split())
    # n：整数の値の範囲（n-1）
    # q：実行されるクエリの数
    # 入力受付
    i = 0
    while i < q:
        try:
            p.append(list(map(int, input().split())))
            i = i + 1
        except:
            break;
    x = UnionFind(n)

    i = 0
    while i < len(p):
        if(p[i][0] == 0):
                x.union(p[i][1],p[i][2])
        if(p[i][0] == 1):
            result = x.same_check(p[i][1],p[i][2])
            if result == False:
                print(0)
            if result == True:
                print(1)

        i = i + 1







if __name__ == '__main__':
    main()


