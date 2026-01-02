MOD = 1000000007

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
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m + x % m) % m

def com(n, k):
    x = 1
    for i in range(k):
        x *= n - i
        x *= mod_inv(i+1,MOD)
        x %= MOD
    return x

n,a,b=map(int,input().split())

x = pow(2, n, MOD)
y = 1 + com(n, a) + com(n, b)
y %= MOD

print((x+MOD-y)%MOD)