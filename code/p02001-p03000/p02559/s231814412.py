class Binary_Indexed_Tree_Exception(Exception):
    pass

class Binary_Indexed_Tree():
    def __init__(self,L,calc,unit,inv):
        """calcを演算とするN項のBinary Indexed Treeを作成

        calc:演算(2変数関数,群)
        unit:群calcの単位元(xe=ex=xを満たすe)
        inv:群calcの逆元(1変数関数)
        """
        self.calc=calc
        self.unit=unit
        self.inv=inv

        N=len(L)
        d=max(1,(N-1).bit_length())
        k=2**d

        X=[None]+[unit]*k

        self.num=k
        self.depth=d

        if L:
            for i in range(len(L)):
                p=i+1
                while p<=k:
                    X[p]=calc(X[p],L[i])
                    p+=p&(-p)
        self.data=X

    def index(self,k,index=1):
        """第k要素の値を出力する.

        k:数列の要素
        index:先頭の要素の番号
        """

        p=k+(1-index)
        return self.sub_array(p,p)

    def add(self,k,x,index=1,right=False):
        """第k要素にxを左から加え,更新を行う.

        k:数列の要素
        x:更新後の値
        index:先頭の要素の番号
        right:「左から」が「右から」になる
        """
        p=k+(1-index)
        while p<=self.num:
            if right==False:
                #左から
                self.data[p]=self.calc(x,self.data[p])
            else:
                #右から
                self.data[p]=self.cal(self.data[p],x)
            p+=p&(-p)

    def update(self,k,x,index=1,right=False):
        """第k要素をxに変え,更新を行う.

        k:数列の要素
        x:更新後の値
        """

        a=self.index(k,index)
        if right==False:
            #左から
            y=self.calc(x,self.inv(a))
        else:
            #右から
            y=self.calc(self.inv(a),x)

        self.add(k,y,index,right)

    def product(self,From,To,index=1):
        """第From要素から第To要素までの総和を求める.

        From:始まり
        To:終わり
        index:先頭の要素の番号
        """
        alpha=max(1,From+(1-index))
        beta=min(self.num,To+(1-index))
        return self.calc(self.inv(self.__section(alpha-1)),self.__section(beta))

    def __section(self,To):
        S=self.unit
        x=To
        while x>0:
            S=self.calc(self.data[x],S)
            x-=x&(-x)
        return S

    def all_product(self):
        return self.data[-1]

#================================================
N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=Binary_Indexed_Tree(A,lambda x,y:x+y,0,lambda x:-x)

X=[]
for _ in range(Q):
    t,u,v=map(int,input().split())
    if t==0:
        B.add(u,v,0)
    else:
        X.append(B.product(u,v-1,0))
print("\n".join(map(str,X)))