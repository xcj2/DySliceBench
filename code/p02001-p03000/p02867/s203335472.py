

# unionfind木構造
# unionfindについてはここhttps://www.slideshare.net/chokudai/union-find-49066733
# グループに属するかの判定(find)や、グループ結合(union)に強い

from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        class KeyDict(dict):
            # 辞書にないときの対応
            def __missing__(self,key):
                self[key] = key
                return key
        self.parent = KeyDict()
        self.rank = defaultdict(int)
        self.weight = defaultdict(int)

    # 根を探す
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            # 経路圧縮
            # 自分自身じゃない場合は、上にさかのぼって検索(再帰的に)
            y = self.find(self.parent[x])           
            self.weight[x] += self.weight[self.parent[x]]   #圧縮時にweightを更新(和)
            self.parent[x] = y      #親の置き換え(圧縮)
            return self.parent[x]

    # 結合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        # 低い方を高い方につなげる(親のランクによる)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    ### 重み付き
    def weighted_union(self, x, y, w):
        # print("unite",x,y,w,self.weight)
        px = self.find(x)
        py = self.find(y)
        # 低い方を高い方につなげる(親のランクによる)
        # if px == py: return 0
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.weight[px] = - w - self.weight[x] + self.weight[y]
        else:
            self.parent[py] = px
            self.weight[py] =  w + self.weight[x] - self.weight[y]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return 0

    # 判定
    def judge(self, x, y):
        return self.find(x) == self.find(y)

N = int(input())
As  = list(map(int, input().split()))
Bs  = list(map(int, input().split()))
As_ind = [(a,i) for i,a in enumerate(As)]
Bs_ind = [(b,i) for i,b in enumerate(Bs)]
As_ind.sort()
Bs_ind.sort()



uf = UnionFind(N)
cnt = 0
for A,B in zip(As_ind,Bs_ind):
    # print(A,B)
    if A[0] > B[0]:
        print("No")
        exit()
    uf.union(A[1],B[1])


d_ans = defaultdict(int)

for i in range(N):
    root = uf.find(i)
    d_ans[root] += 1
if len(d_ans) >= 2:
    print("Yes")
else:
    # サイクルが1つの場合
    # 巡回置換は、どこかをswapするとそこでcycleが分解されるので、swapしても結果に影響がないかを判断する
    # 具体的には A_p(i+1) <= B_i になっているならば、A_pi, A_p(i+1)をswapしても結果は変わらない。それを比べる。
    for i in range(1,N):
        if As_ind[i][0] <= Bs_ind[i-1][0]:
            print("Yes")
            exit()
    print("No")