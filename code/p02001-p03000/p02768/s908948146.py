# D
#入力
n,a,b=map(int,input().split())

#諸関数
def pront(X):
    #デバッグ用プリント
    #環境変数としてdebugを確保して、それが1なら内容を出力
    if debug==0:
        print(X)

#デバッグ用
debug=1#0:本番,1:デバッグ中

#処理
#定数
base=(10**9)+7

#関数
    #10*9+7で割ったあまりを返し続ける
def add(a,b):#a+b
    return(((a%base)+(b%base))%base)
def sub(a,b):#a-b
    return (((a%base)-(b%base))%base)
def multi(a,b):#a*b
    return(((a%base)*(b%base))%base)
def exp(a,b):#a**b
    x=1
    c=a
    d=b
    while d!=0:
        if d%2==1:
            x=multi(x,c)
        c=(c**2)%base
        d=d//2
    return x

#割り算はフェルマーの小定理に基づいて考える
def div(a,b):#a/b
    return(multi(a,exp(b,base-2)))

    #その他演算
def fact(m,n):#m~nの積(m<n)
    x=1
    for i in range(m,n+1):
        x=multi(x,i)
    return x
def comb(n,r):
    return div(fact(n-r+1,n),fact(1,r))
#処理
Z=sub(sub(sub(exp(2,n),comb(n,a)),comb(n,b)),1)
print(Z)