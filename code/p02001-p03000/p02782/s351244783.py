MOD = 10**9+7
p= []
rp = []

def g(r,c):
    ans = 0
    if r > c:
        r,c = c,r
    for i in range(r+1):
        ans += f(i+1,c)
        ans %= MOD
    return ans

def f(r,c):
    return (p[r+c] * rp[r] * rp[c]) % MOD

def extgcd(a,b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2]//w[2]
        ra = w
        wa = [r[0]-q*w[0], r[1]-q*w[1], r[2]-q*w[2]]
        r = ra
        w = wa
    #[x,y]
    return [w[0], w[1]]

def mod_inv(a,m):
    x = extgcd(a, m)[0]
    return (m+x%m)%m

r1,c1, r2,c2 = map(int,input().split())
p = [0 for _ in range(r2+c2+3)]
rp = [0 for _ in range(max(r2,c2)+2)]

p[0] = 1
p[1] = 1
rp[0] = 1
rp[1] = 1
for i in range(2,c2+r2+3):
    p[i] = (p[i-1] * i) % MOD

for i in range(2,max(r2,c2)+2):
    rp[i] = mod_inv(p[i], MOD)

ans = g(r2,c2) - g(r1-1,c2) - g(r2,c1-1) + g(r1-1,c1-1)
ans %= MOD
print (ans)