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
    X,Y=mi()
    MOD = 10**9+7
    C = Counting(10**6+10,MOD)
    ans = 0
    for a in range(X+1):
        if (X-a) %2 == 1: continue
        b = (X-a)//2

        if 2*a+b == Y:
            ans += C.nCk(a+b,a)
    
    print(ans)






if __name__ == "__main__":
    main()