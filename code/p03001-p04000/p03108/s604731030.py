class UnionFind:
    def __init__(self,n):
        #木の親要素　par[x]=xならxは根。par[x]=1ならxの親は1
        #最初は全員自分の親は自分
        self.par = [i for i in range(n+1)]
        #要素数
        self.elm = [0]+[1]*(n)
        #木の高さを格納(1:木は低いほうがいい　2:親要素の書き換えは少ないほうがいい)
        #低->高
        self.rank = [0]*(n+1)
        
    #探索
    def find(self,x):
        #根ならその番号を返す
        if self.par[x] == x:
            return x
        
        #根でないなら親の要素で再検索
        else:
            #走査していく過程で親を書き換える(これで同じグループでは全員同じ親)
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        
    #併合
    def union(self,x,y):
        #根を探す
        x = self.find(x)
        y = self.find(y)
        #木の高さを比較し、低いほうから高い方に辺を張る
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.elm[y] += self.elm[x]
        else:
            self.par[y] = x
            self.elm[x] += self.elm[y]
        #木の高さが同じならば片方を1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    #同じ集合に属するか判定
    def same_check(self,x,y):
        return self.find(x) == self.find(y)
    
    #xが属する木のサイズを返す
    def count(self,x):
        return self.elm[self.find(x)]
    
    
def conne(n):
    return n*(n-1)//2

n,m=map(int,input().split())
AB=[tuple(map(int,input().split())) for i in range(m)]
AB=AB[::-1]

uc=conne(n)
unconv=[uc]
conv=0

# n個の島、橋は0
uf=UnionFind(n)

ufsc=uf.same_check
ufu=uf.union
ufc=uf.count

unconv_app=unconv.append


for ab in AB:
    a=ab[0]
    b=ab[1]
    if conv<uc:
        #aとbが属する木が異なる
        if ufsc(a,b)==False:
            #aが属する木と、bが属する木を併合
            conv-=conne(ufc(a))
            conv-=conne(ufc(b))
            ufu(a,b)
            conv+=conne(ufc(a))
       
    unconv_app(uc-conv)
    
unconv.pop()
unconv=unconv[::-1]

for i in range(m):
    print(unconv[i])