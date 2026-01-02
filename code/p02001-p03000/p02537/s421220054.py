class Segment_Tree():
    """
    このプログラム内は1-index
    """

    def __init__(self,L,calc,unit):
        """calcを演算とするリストLのSegment Treeを作成

        calc:演算(2変数関数,モノイド)
        unit:モノイドcalcの単位元 (xe=ex=xを満たすe)
        """
        self.calc=calc
        self.unit=unit

        N=len(L)
        d=max(1,(N-1).bit_length())
        k=1<<d

        self.data=[unit]*k+L+[unit]*(k-len(L))
        self.N=k
        self.depth=d

        for i in range(k-1,0,-1):
            self.data[i]=calc(self.data[i<<1],self.data[i<<1|1])

    def get(self,k,index=1):
        """第k要素を取得
        """
        assert 0<=k-index<self.N,"添字が範囲外"
        return self.data[k-index+self.N]

    def update(self,k,x,index=1):
        """第k要素をxに変え,更新を行う.

        k:数列の要素
        x:更新後の値
        """
        assert 0<=k-index<self.N,"添字が範囲外"
        m=(k-index)+self.N
        self.data[m]=x

        while m>1:
            m>>=1
            self.data[m]=self.calc(self.data[m<<1],self.data[m<<1|1])


    def product(self,From,To,index=1,left_closed=True,right_closed=True):
        L=(From-index)+self.N+(not left_closed)
        R=(To-index)+self.N+(right_closed)

        vL=self.unit
        vR=self.unit

        while L<R:
            if L&1:
                vL=self.calc(vL,self.data[L])
                L+=1

            if R&1:
                R-=1
                vR=self.calc(self.data[R],vR)

            L>>=1
            R>>=1

        return self.calc(vL,vR)

    def all_prod(self):
        return self.data[1]
#================================================
N,K=map(int,input().split())
A=[0]*N
for i in range(N):
    A[i]=int(input())

T=max(A)
S=Segment_Tree([0]*(T+1),max,0)
DP=[0]*N

for i in range(N-1,-1,-1):
    X=S.product(max(0,A[i]-K),min(T,A[i]+K),0)
    DP[i]=X+1
    S.update(A[i],X+1,0)

print(max(DP))