# コンビネーション
mod = 10**9+7
def cmb(n, r, mod=mod):
    ret = 1
    for k in range(1, r+1):
        ret = ret * (n-k+1) * mod_inv(k) % mod
    return ret

# modを取りながらべき乗する
def power_func(a,n,mod=mod):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %mod
        if bi[i]=="1":
            res=(res*a) %mod
    return res

#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m=mod):
    x = extgcd(a,m)[0]
    return (m+x%m)%m


import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
ans = (power_func(2, N) - 1 - cmb(N, A) - cmb(N, B))%mod
print(ans)