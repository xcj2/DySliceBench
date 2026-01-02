import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    ################
    class UnionFind():
        """
        parents : 親要素(findしない場合は根ではないことの注意)，根の場合は"-(要素数）"
        find(x):要素xの属するグループの根を返す
        size(x):要素xの属するグループの要素数を返す
        same(x,y):x,yが同じグループに属しているか返す
        重いかも！　　members(x):要素xが属するグループに属する要素をリストで返す
        roots:全ての根の要素を返す
        group_count():グループの数を返す
        重いかも！　all_group_members():{根要素：[そのグループに含まれる要素のリスト]}の辞書を返す
        """
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

        def find(self, x):
            #根を探す&つなぎかえる
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.parents[x] > self.parents[y]:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def size(self, x):
            return -self.parents[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def group_count(self):
            return len(self.roots())

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    ################


    mod=10**9+7
    N,K=MI()
    P=LI()
    C=LI()
    
    for i in range(N):
        P[i]-=1
    
    uf =UnionFind(N)
    for i in range(N):
        uf.union(i,P[i])
        
    from collections import defaultdict
    dd = defaultdict(list)
        
    for i in range(N):
        root=uf.find(i)
        dd[root]+=[i]
        
    ansAll=-1*(10**10)
    for k,v in dd.items():
        N2=len(v)
        #rootから移動した時の点数の順番，3周分
        L=[0]*(3*N2+3)
        now=k
        for i in range(3*N2+3):
            nxt=P[now]
            L[i]=C[nxt]
            now=nxt
        S=[0]*(3*N2+3)
        for i in range(3*N2+2):
            S[i+1]=S[i]+L[i]
        
        ans=0
        
        ROOP=S[N2]-S[0] 
        if ROOP>0:#1週分
            roop=max(K//N2-1,0)#1周分が+でも最後の1つをとらない方が良いみたいなことも
            ans+=ROOP*roop
            rem=K-roop*N2
        else:
            roop=0
            rem=min(K,N2)
            
        if roop==0:
            temp=-1*(10**10)
        else:
            #1回以上ループしていれば，追加で1こも取る必要はない
            temp=0
        for i in range(1,rem+1):#i個トル
            for j in range(N2+1):#jからスタート
                s=S[j+i]-S[j]
                temp=max(temp,s)
        ans=ans+temp
        
        # print(k,v,roop,rem)
        # print(L)
        # print(S)
        # print(temp,ans)
        # print("---")
        
        
        ansAll=max(ansAll,ans)
        
    print(ansAll)
        
            
    
 
        
    
            
    

main()
