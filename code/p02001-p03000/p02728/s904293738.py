#%%
import sys
sys.setrecursionlimit(10**7) #再帰関数の上限,10**5以上の場合python
import math
from collections import deque 
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone
#import fractions#古いatcoderコンテストの場合GCDなどはここからimportする
from functools import lru_cache#pypyでもうごく
#@lru_cache(maxsize = None)#maxsizeは保存するデータ数の最大値、2**nが最も高効率


def input(): return sys.stdin.readline()[:-1]
def printl(li): _=print(*li, sep="\n") if li else None
def argsort(s, return_sorted=False): 
    inds=sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted: return inds, [s[i] for i in inds]
    return inds
def alp2num(c,cap=False): return ord(c)-97 if not cap else ord(c)-65
def num2alp(i,cap=False): return chr(i+97) if not cap else chr(i+65)
def matmat(A,B):
    K,N,M=len(B),len(A),len(B[0])
    return [[sum([(A[i][k]*B[k][j]) for k in range(K)]) for j in range(M)] for i in range(N)]
def matvec(M,v):
    N,size=len(v),len(M)
    return [sum([M[i][j]*v[j] for j in range(N)]) for i in range(size)]
def T(M):
    n,m=len(M),len(M[0])
    return [[M[j][i] for j in range(n)] for i in range(m)]

    
class modint:#add:和,mul:積,pow:累乗,div:商(modと互いに素であること)
    def __init__(self,x,mod=1000000007): 
        if isinstance(x, modint):x=x.x
        self.x, self.mod= x%mod, mod

    def __str__(self):
        return str(self.x)

    def __add__(self, a):
        if isinstance(a, modint):a=a.x
        return modint(self.x+a,self.mod)

    def __radd__(self, a):return self.__add__(a)

    def __iadd__(self, a):
        self.x=self.__add__(a)
        return self

    def __sub__(self, a):
        if isinstance(a, modint):a=a.x
        return self.__add__(-a)
    
    def __rsub__(self, a):return (a-self.x)%self.mod

    def __isub__(self, a):
        return self.__iadd__(-a)

    def __mul__(self, c):
        if isinstance(c, modint):c=c.x
        return modint(self.x*(c%self.mod),self.mod)
    
    def __rmul__(self, c):return self.__mul__(c)
    
    def __imul__(self, c):
        return self.__mul__(c)

    def __pow__(self,p):
        if isinstance(p, modint):p=p.x
        return modint(pow(self.x,p,self.mod),self.mod)
    
    def __ipow__(self,p):
        return self.__pow__(p)
        

    def __truediv__(self, d):
        if isinstance(d, modint):d=d.x
        u,v,a,b=1,0,d,self.mod
        while b:
            t=a//b
            a-=t*b
            a,b,u,v=b,a,v,u-t*v
        if a!=1: print("not 素")
        return modint(self.x*(u%self.mod),self.mod)

    def __itruediv__(self, d):
        self.x=self.__truediv__(d)
        return self

    def __eq__(self, target):
        if isinstance(target, modint):
            return self.x==target.x
        return self.x==target%self.mod
    
        
class comb:
    def __init__(self,N,mod=10**9+7):#コンビネーションnCrをmodで求める、Nは最大のn 
        self.mod=mod
        self.fact=[0]*(N+1)
        self.ifact=[0]*(N+1)
        fact,ifact=self.fact,self.ifact
        fact[0],fact[1],ifact[0],ifact[1]=1,1,1,1
        for i in range(2,N+1):
            x=(fact[i-1]*i)%mod
            fact[i]=x
            ifact[i]=self.extgcd1(x,mod)
        

    #@lru_cache(maxsize = None)
    def extgcd1(self,a0,b0):#計算量log(b0),フェルマーの小定理より早い
        u,v,a,b=1,0,a0,b0
        while b:
            t,a=divmod(a,b)
            a,b,u,v=b,a,v,u-t*v
        if a!=1: 
            print("not 素")
            return -1
        return u%b0

    #@lru_cache(maxsize = None)
    def comb(self,n,r): return (self.fact[n]*self.ifact[r]%self.mod)*self.ifact[n-r]%self.mod

    #@lru_cache(maxsize = None)
    def mulcomb(self,n,*rs):#n!/(r1!*r2!*r3!*...)
        ans=self.fact[n]
        for r in rs: ans=(ans*self.ifact[r])%self.mod
        return ans

class rerooting:#全方位木
    def __init__(self,N,edge):#単位元self.unitとモノイドdef funcを設定すること,
        #dics[親][根（親の隣接点)]=その部分木での値
        self.unit=(modint(1),0)
        self.mod=10**9+7
        self.edge=edge
        self.cb=comb(N)
        self.fact=self.cb.fact
        self.ifact=self.cb.ifact
        self.par=[-1]*N
        self.N=N
        self.visited=[0]*N
        self.dics=[dict() for _ in range(N)]
        self.ikigake=[]
        self.tot=[self.unit]*N
    
    #@lru_cache(maxsize = None)
    def func(self,x,y):
        #ifact=self.ifact
        #mod=self.mod
        p1,s1=x
        p2,s2=y
        ans=modint(p1*p2)
        ssum=s1+s2
        ans*=self.cb.comb(ssum,s1)
        #ans*=(self.fact[ssum]*self.ifact[s1])%self.mod*self.ifact[s2]%self.mod
        #ans%=self.mod
        return ans,ssum 

    def addnode(self,x):#部分木に親のノードを結合する処理,dfsとforwardに出現
        return x[0],x[1]+1

    # def _dfs(self,e,pa):
    #     edge=self.edge
    #     self.par[e]=pa
    #     self.ikigake.append(e)
    #     ans=self.unit
    #     for ne in edge[e]:
    #         if self.par[ne]!=-1:
    #             continue
    #         ans=self.func(ans,self.addnode(self._dfs(ne,e)))
    #         #print(ans)
    #     if pa!=e:
    #         self.dics[pa][e]=ans
        
    #     return ans
    def _dfs(self,start):
        edge=self.edge
        N=self.N
        par=self.par
        q=deque([(start,start)])
        while len(q):
            e,pa=q.pop()#ここをpopleftにすると幅優先探索BFSになる
            if par[e]!=-1:continue
            par[e]=pa
            self.ikigake.append(e)
            for ne in edge[e]:q.append((ne,e))
        
        for e in reversed(self.ikigake[1:]):
            pa=par[e]
            ans=self.unit
            de=self.dics[e]
            for val in de.values():
                ans=self.func(ans,self.addnode(val))
            self.dics[pa][e]=ans

    def forward(self,start):
        self._dfs(start)
        #print(t2-t1)
        #count=0
        for e in self.ikigake:
            pa=self.par[e]
            de=self.dics[e]
            nes=tuple(de.keys())
            nvals=tuple(de.values())
            l=len(nes)
            aleft=[self.unit]
            aright=[self.unit]
            cleft=self.unit
            cright=self.unit
            for i in range(l-1):
                aleft.append(self.func(aleft[-1],self.addnode(nvals[i])))
                aright.append(self.func(aright[-1],self.addnode(nvals[-i-1])))
                #count+=4
            #print(e,l,self.dics)
            self.tot[e]=self.func(aright[-1],self.addnode(nvals[0]))
            for i,ne in enumerate(nes):
                if ne==pa:
                    continue
                self.dics[ne][e]=self.func(aleft[i],aright[-1-i])
                #count+=1
        #print(t3-t2)

def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    N = int(input())
    #N, K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列

    def tree_init(N):
        edgelist = [[] for _ in range(N)]
        elist=set()
        for a, b in [map(int, input().split()) for i in range(N-1)]:#木じゃない場合N-1をNに変える
            edgelist[a-1].append(b-1)#ノードの番号が0から始まる場合-1を消す
            edgelist[b-1].append(a-1)
            elist.add((a-1,b-1))
        return edgelist,elist

    edge,elist=tree_init(N)
    cb=comb(N)
    rt=rerooting(N,edge)
    rt.forward(0)

    for a in range(N):
        print(rt.tot[a][0])

if __name__ == "__main__":
    main()

#%%