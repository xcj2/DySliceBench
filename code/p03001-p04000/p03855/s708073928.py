from collections import*
import sys
input=sys.stdin.readline


class UNION_FIND(object):
    def __init__(self,n):
        #親の番号を格納する。親だった場合は-(その集合のサイズ)
        #作るときはParentの値を全て-1にする
        #こうすると全てバラバラになる
        self.parent=[-1 for i in range(n)]
        
    def root(self,x):
        #Aがどのグループに属しているか調べる
        if self.parent[x]<0:
            return x
        else:
            self.parent[x]=self.root(self.parent[x])  #親を再帰で探知 再帰は最後に上のifにひっかかる
            return self.parent[x]
 
    def size(self,x):
        #自分のいるグループの頂点数を調べる
        return -self.parent[self.root(x)]   #親をとってきたい
        
    def union(self,x,y):
        #AとBをくっ付ける
        #AとBを直接つなぐのではなく、root(A)にroot(B)をくっつける
        #print(self.parent)
        x=self.root(x)
        y=self.root(y)
        #print(x,y)
        if x==y:   #すでにくっついてるからくっ付けない
            return False
            
        #大きい方(A)に小さいほう(B)をくっ付けたい
        #大小が逆だったらひっくり返しちゃう。
        if self.size(x)<self.size(y):
            x,y=y,x
        self.parent[x]+=self.parent[y]  #Aのサイズを更新する
        self.parent[y]=x   #Bの親をAに変更する
        return True
        
n,k,l=map(int,input().split())
u1=UNION_FIND(n)
u2=UNION_FIND(n)
d=defaultdict(int)
for i in range(k):
    p,q=map(int,input().split())
    u1.union(p-1,q-1)
for i in range(l):
    p,q=map(int,input().split())
    u2.union(p-1,q-1)
for i in range(n):
    d[(u1.root(i),u2.root(i))]+=1
print(*[d[(u1.root(i),u2.root(i))]for i in range(n)])