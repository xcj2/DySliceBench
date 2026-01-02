import sys
sys.setrecursionlimit(10**6)
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


#(a/b)をmで割った余りを求める
#b^(-1)にaを掛けたものをmで割ればよい

def div_remainder(a,b,m):
    b_inv=gyakugen(b,m)
    a%=m
    return (a*b_inv)%m


#(a*b)をmで割った余りを求める

def multi_remainder(a,b,m):
    a%=m
    b%=m
    return (a*b)%m



#nPrをmで割った余りを求める(ただしn<m、mは素数)

def perm_remainder(n,r,m):
    if r>1:
      return (perm_remainder(n-1,r-1,m)*n)%m
    elif r==1:
      return n
    else:
      return 1

#nCrをmで割った余りを求める(ただしn<m,mは素数)

def comb_remainder(n,r,m):
    r=min(r,n-r)
    return (perm_remainder(n,r,m)*gyakugen(perm_remainder(r,r,m),m))%m


x,y=map(int,input().split())
m=10**9+7
if (2*x-y)%3!=0 or (-x+2*y)%3!=0 or 2*x-y<0 or -x+2*y<0:
  ans=0
else:
  nx=(2*x-y)//3
  n=(x+y)//3
  ans=comb_remainder(n,nx,m)
print(ans)