import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    from collections import defaultdict
    #nの素因数分解，[[a1,b1],[a2,b2]...]   aがb個,
    def factorization(n):
        if n==1:
            return [[1,0]]
        arr = []
        temp = n
        for i in range(2, int(-(-n**0.5//1))+1):
            if temp%i==0:
                cnt=0
                while temp%i==0:
                    cnt+=1
                    temp //= i
                arr.append([i, cnt])

        if temp!=1:
            arr.append([temp, 1])

        if arr==[]:
            arr.append([n, 1])

        return arr
    
    lcm_dd = defaultdict(int)
    
    N=I()
    A=LI()
    for i in range(N):
        a=A[i]
        arr=factorization(a)
        for v in arr:
            p,cnt=v
            lcm_dd[p]=max(lcm_dd[p],cnt)
            
    lcm=1
    for k,v in lcm_dd.items():
        temp=pow(k,v,mod)
        lcm=(lcm*temp)%mod
        
    ans=0
    for i in range(N):
        temp=(lcm*pow(A[i],mod-2,mod))%mod
        ans=(ans+temp)%mod
        
    print(ans%mod)
        
    


main()
