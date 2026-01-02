class UnionFind:
    """
    - sizeを指定
    - 要素をグループにまとめる(unite) 
    - 要素同士が同じグループか判定する(isSame)
    - 分離はできない
    - par: 親の番号(はじめ par[i]==i つまりすべての頂点が根)
    - 始め各要素は別々のグループ"""
    def __init__(self, size: int):
        self.par = [-1]*size
        for i in range(size):
            self.par[i] = i 
    
    def root(self, x: int) -> int:
        """根を求める"""
        if self.par[x] == x: # if root
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]
    
    def isSame(self, x:int, y:int)->bool:
        """x と y が同じ集合に属するか否か"""
        return self.root(x)==self.root(y)
    
    def unite(self, x:int, y:int):
        """x と y の属する集合を併合"""
        x = self.root(x)
        y = self.root(y)
        if x == y: return
        self.par[x] = y


H,W = map(int, input().split())
s = [input() for _ in range(H)]
uf = UnionFind(H*W) 

def pos2int(h,w):
    # 座標->[0 - H*W]
    return h*W + w

for h in range(H):
    for w in range(W):        
        for dh, dw in zip((0, 1), (1, 0)):
            if not(0<=h+dh<H and 0<=w+dw<W):
                continue
            if s[h][w] != s[h+dh][w+dw]: # 同じグループにする
                uf.unite(pos2int(h, w), pos2int(h+dh, w+dw))
                
white = [0] * H*W
black = [0] * H*W
 
for h in range(H):
    for w in range(W):
        n = pos2int(h, w)
        r = uf.root(n)
        # print(n, r)
        if s[h][w] == ".":
            white[r] += 1
        else:
            black[r] += 1
# print(white)
# print(black)
ans = 0
for h in range(H):
    for w in range(W):
        n = pos2int(h, w)
        ans += white[n] * black[n]
print(ans)