import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,M = LI()
AB = [LI() for i in range(M)]
del AB[0]

AB.reverse()

# 逆に橋がない状態から1本ずつ橋を加えた時に、不便さがどのくらい減少するかを考える

class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n+1)]  # 親のノード番号
        self.rank = [0]*(n+1)
    def find(self,x):  # xの根のノード番号
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def same_check(self,x,y):  # x,yが同じグループか否か
        return self.find(x) == self.find(y)
    def unite(self,x,y):  # x,yの属するグループの併合
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            x,y = y,x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x

G = UnionFind(N)
C = [1]*(N+1)  # 連結成分の大きさ(根となっている頂点だけ正しい)

ANS = [N*(N-1)//2]
for a,b in AB:
    if not G.same_check(a,b):
        x = C[G.find(a)]
        y = C[G.find(b)]
        ANS.append(ANS[-1]-x*y)  # 連結成分の積だけ不便さが減少
        G.unite(a,b)
        C[G.find(a)] = x+y  # 連結成分の大きさを変える
    else:
        ANS.append(ANS[-1])

ANS.reverse()

print(*ANS,sep='\n')
