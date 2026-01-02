n, m = list(map(int, input().split()))
data = dict()
div = 2
mod = 10**9+7
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
#a/b = a*(b`)となるb`を求める
def mod_inv(a,mod):
    x = extgcd(a,mod)[0]
    return (mod+x%mod)%mod
def mod_factorial(n):
    ans = 1
    while n >= 2:
        ans  = (ans * n) % mod
        n -= 1
    return ans
while m > 1:
    count = 0
    flag = False
    while m % div == 0:
        if div not in data:
            data[div] = 0
        flag = True
        m /= div
        count += 1
        data[div] += 1
    div += 1
ans = 1
for i in data.keys():
    p = mod_factorial(data[i]+n-1)
    q = mod_inv(mod_factorial(data[i]), mod)
    r = mod_inv(mod_factorial(n-1), mod)
    ans *= p * q
    ans %= mod
    ans *= r
    ans %= mod
print(ans)
