from collections import defaultdict

# UnionFind
class UnionFind():
    # 作りたい要素数nで初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if(self.root[x] < 0):
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
        if(x == y):
            return 
        # 違う木に属していた場合rnkを見てくっつける方を決める
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return -self.root[self.Find_Root(x)]

# solution
N,M,K=list(map(int,input().split()))
group=UnionFind(N)
friend=defaultdict(int)
for _ in range(M):
    src,dst=list(map(int,input().split()))
    group.Unite(src-1,dst-1)
    friend[src-1]+=1
    friend[dst-1]+=1

block=defaultdict(list)
for _ in range(K):
    src,dst=list(map(int,input().split()))
    block[src-1].append(dst-1)
    block[dst-1].append(src-1)

ans=[]
for i in range(N):
    total=group.Count(i)
    num=total-1-friend[i]
    #remove block
    for b in block[i]:
        if group.isSameGroup(i,b):
            num-=1
    ans.append(num)

for i in ans:
    print(i,end=" ")
print()


