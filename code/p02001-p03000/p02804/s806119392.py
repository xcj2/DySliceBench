mod = 10**9+7
memo = dict()
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
factorial = [1 for i in range(n+1+k)]
for i in range(1,n+1+k):
    factorial[i] = (factorial[i-1] * i) % mod
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
def mod_combination(n,k,mod):
    if n < k:
        return 0
    return factorial[n] * mod_inv(factorial[n-k], mod) * mod_inv(factorial[k], mod)
ans = 0
for i in range(n):
    #今回の数字が、最小値として数えられる数の合計
    ans -= a[i] * mod_combination(n - i - 1, k-1,mod)
    #今回の数字が、最大値として数えられる数の合計
    ans += a[i] * mod_combination(i,k-1,mod)
    ans %= mod
print(int(ans))