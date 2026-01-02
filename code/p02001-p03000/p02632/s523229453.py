import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20

class Counting():
    def __init__(self,maxim,mod):
        maxim += 1

        self.mod = mod
        self.fact = [0]*maxim
        self.fact[0] = 1
        for i in range(1,maxim):
            self.fact[i] = self.fact[i-1] * i % mod

        self.invfact = [0]*maxim
        self.invfact[maxim-1] = pow(self.fact[maxim-1],mod-2,mod)
        for i in reversed(range(maxim-1)):
            self.invfact[i] = self.invfact[i+1] * (i+1) % mod


    def nCk(self,n,r):
        if n < 0 or n < r: return 0
        return self.fact[n] * self.invfact[r] * self.invfact[n-r] % self.mod

    def nPk(self,n,r):
        if n < 0 or n < r: return 0
        return self.fact[n] * self.invfact[n-r] % self.mod




def main():
    K=ii()
    S=list(input())
    N=len(S)
    MOD = 10**9+7

    comb = Counting(N+K+10,MOD)
    ans = 0
    for x in range(K+1):
        ans += comb.nCk(N+K-(x+1),N-1) * pow(25,K-x,MOD) * pow(26,x,MOD) % MOD
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()