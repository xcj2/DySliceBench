import sys
import math
input = sys.stdin.readline
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

x,y=MI()
if y>2*x or x>2*y:
    print(0)
    sys.exit()
elif x%3==0 and y%3==0:
    m=x//3
    l=y//3
    print(cmb(m+l,2*l-m,mod))
    
elif x%3==1 and y%3==2:
    m=(x-1)//3
    l=(y-2)//3
    print(cmb(m+l+1,2*l-m+1,mod))
elif x%3==2 and y%3==1:
    m=(x-2)//3
    l=(y-1)//3
    print(cmb(m+l+1,2*l-m,mod))
else:
    print(0)
