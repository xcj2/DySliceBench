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
    S=ii()
    MOD = 10**9+7

    k = 1
    ans = 0
    C = Counting(10**6,MOD)
    while S-3*k >= 0:
        ans += C.nCk(S-2*k-1,k-1)
        ans %= MOD
        k += 1
    
    print(ans%MOD)



if __name__ == "__main__":
    main()