import sys
def input():
    return sys.stdin.readline()[:-1]
n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=10**9+7

class Combination:
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)
 
    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod
 
    def make_factorial_list(self, n):
 
        fac = [1]
        facinv = [1]
        for i in range(1, n+1):
            fac.append(fac[i-1] * i % self.mod)
            facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
        return fac, facinv
 
    def make_modinv_list(self, n):
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
        return modinv

a.sort()
ans=0
if n==1 or k==1:
    print(0)
    exit()
# c=cmb(n-1,k-1,mod)
comb = Combination(10**5)
# for i in range(n):
#     print(a[i]-low)
#     suuji[a[i]-low][0]+=i
#     suuji[a[i]-low][1]+=c-i

for i in range(len(a)):
    if i>=k-1:
        ans+=a[i]*comb(i,k-1)
        ans%=mod
    if n-i-1>=k-1:
        ans-=a[i]*comb(n-i-1,k-1)
        ans%=mod
    ans%=mod
# print(suuji)
print(ans)