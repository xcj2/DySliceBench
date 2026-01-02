import sys
def input(): return sys.stdin.readline().rstrip()
class Sieve: #区間[2,n]の値の素因数分解
    def __init__(self,n=1):
        self.primes=[]
        self.f=[0]*(n+1) #ふるい（素数ならその値）
        self.f[0]=self.f[1]=-1
        for i in range(2,n+1): #素数リスト作成
            if self.f[i]: continue
            self.primes.append(i)
            self.f[i]=i
            for j in range(i*i,n+1,i):
                if not self.f[j]:
                    self.f[j]=i  # 最小の素因数を代入
    def is_prime(self, x):
        return self.f[x]==x
    def prime_fact(self,x): # 素因数分解の昇順リスト, {2:p,3:q,5:r,...}
        fact_dict=dict()
        while x!=1:
            p=self.f[x]
            fact_dict[p]=fact_dict.get(p,0)+1
            x//=self.f[x]
        return fact_dict

def main():
    n=int(input())
    A=list(map(int,input().split()))
    mod=10**9+7
    p_lis={}
    Prime=Sieve(10**6+5)
    for a in A:
        f=Prime.prime_fact(a)
        #print(f)
        for key in f:
            p_lis[key]=max(p_lis.get(key,0),f[key])
    lcm=1
    #print(p_lis)
    for key in p_lis:
        lcm=(lcm*pow(key,p_lis[key],mod))%mod
    ans=0
    #print(lcm)
    for a in A:
        b=lcm*pow(a,mod-2,mod)%mod
        ans=(ans+b)%mod
    print(ans)


if __name__ == '__main__':
    main()

