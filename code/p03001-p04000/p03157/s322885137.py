from itertools import groupby

class UnionFindVerSize():
    def __init__(self, N):
        global S,H,W
        """ N個のノードのUnion-Find木を作成する """
        # 親の番号を格納する。自分が親だった場合は、自分の番号になり、それがそのグループの番号になる
        self._parent = [n for n in range(0, N)]
        # グループのサイズ（個数）
        self._size = [1] * N

        self._black=[0]*N
        self._white=[0]*N

        for i in range(0,H*W):
            h=i//W
            w=i%W
            if S[h][w]=='#':
                self._black[i]=1
                self._white[i]=0
            else:
                self._black[i]=0
                self._white[i]=1

    def find_root(self, x):
        """ xの木の根(xがどのグループか)を求める """
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x]) # 縮約
        return self._parent[x]

    def unite(self, x, y):
        """ xとyの属するグループを併合する """
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        # 小さい方を大きい方に併合させる（木の偏りが減るので）
        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._black[gy]+=self._black[gx]
            self._white[gy]+=self._white[gx]
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._black[gx]+=self._black[gy]
            self._white[gx]+=self._white[gy]
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        """ xが属するグループのサイズ（個数）を返す """
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        """ xとyが同じ集合に属するか否か """
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        """ グループ数を計算して返す """
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans

    def calc_black(self,x):
        return self._black[self.find_root(x)]

    def calc_white(self,x):
        return self._white[self.find_root(x)]


H,W=map(int,input().split())
S=[]
for i in range(0,H):
    s=input()
    S.append(s)

uf=UnionFindVerSize(H*W)
for i in range(0,H*W):
    h=i//W
    w=i%W
    if W-1>=w+1:
        if S[h][w]!=S[h][w+1]:
            uf.unite(i,i+1)
    if H-1>=h+1:
        if S[h][w]!=S[h+1][w]:
            uf.unite(i,i+W)

root=[uf.find_root(i) for i in range(0,H*W)]
root.sort()

ans=0
root=groupby(root)
for key,group in root:
    black=uf.calc_black(key)
    white=uf.calc_white(key)
    ans+=black*white

print(ans)
