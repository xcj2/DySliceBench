import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n+1)]  # 親のノード番号
        self.rank = [0]*(n+1)
        self.X = [0]+[1]*n
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
        self.X[x] = self.X[x]+self.X[y]


N,M = MI()
UF = UnionFind(N)
AB = [tuple(MI()) for _ in range(M)]
AB.reverse()

ans = N*(N-1)//2
ANS = []
for i in range(M):
    ANS.append(ans)
    a,b = AB[i]
    if UF.same_check(a,b):
        continue
    else:
        ans -= UF.X[UF.find(a)]*UF.X[UF.find(b)]
        UF.unite(a,b)

ANS.reverse()
print(*ANS,sep='\n')
