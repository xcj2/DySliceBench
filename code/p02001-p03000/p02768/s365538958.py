n,a,b=map(int,input().split())
m=10**9+7

#(a*x)をmで割った余りが1になるようなxを求める
#aで割ったときの余りはa^(-1)をかけた余りと同じ
#逆元a^(-1)を求める
#aとmが互いに素であることが条件

def gyakugen( a, m ):
  b = m
  x, y = 1, 0
  while b>0:
    q = a // b
    a, b = b, a-q*b
    x, y = y, x-q*y
  return x if x>0 else x+m

#nPrをmで割った余りを求める(ただしn<m、mは素数)
import sys
sys.setrecursionlimit(10**9)#再帰の回数の上限を設定

def perm_remainder(n,r,m):
    if r>=1:
        return (perm_remainder(n-1,r-1,m)*n)%m
    else:
        return 1

#nCrをmで割った余りを求める(ただしn<m,mは素数)

def comb_remainder(n,r,m):
    r=min(r,n-r)
    return (perm_remainder(n,r,m)*gyakugen(perm_remainder(r,r,m),m))%m

#(a**n)を素数mで割った余りを求める
#当然aはmで割り切れない整数

def power_remainder(a,x,m):
    a=a%m
    bi=str(format(x,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %m
        if bi[i]=="1":
            res=(res*a) %m
    return res

#2^n-nCa-nCb-1を計算
print((power_remainder(2,n,m)-1-comb_remainder(n,a,m)-comb_remainder(n,b,m))%m)