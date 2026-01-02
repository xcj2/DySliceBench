class Factorial():
    def __init__(self,n,mod):
        self.mod = mod
        self.factorial = [0 for _ in range(n+1)]
        self.inv = [0 for _ in range(n+1)]
        self.factorial[0] = 1
        self.inv[0] = 1
        for i in range(n):
            self.factorial[i+1] = self.factorial[i]*(i+1)%mod
        self.inv[n] = pow(self.factorial[n],mod-2,mod)
        for i in range(n)[::-1]:
            self.inv[i] = self.inv[i+1]*(i+1)%mod


    def comb(self,m,k): #組み合わせ 0<=k<=m<=n
        return self.factorial[m]*self.inv[k]*self.inv[m-k]%self.mod

def solve():

    MOD = 1000000007

    r1,c1,r2,c2 = map(int,input().split())

    f = Factorial(2000010,MOD)

    ans = 0

    for i in range(r2-r1+1):
        ans += f.comb(r1+c2+i+1,r1+i+1)-f.comb(r1+c1+i,r1+i+1)
        ans %= MOD

    print(ans)

solve()