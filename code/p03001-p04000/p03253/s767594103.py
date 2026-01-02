import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    MOD = 10**9+7
    
    def factorization(n):
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

        return arr
        
    cl = factorization(M)
    
    def combinations(x,y,N):
        fac = [0]*(N+1)
        fac[0],fac[1] = 1,1
        
        for i in range(2,N+1):
            fac[i] = (fac[i-1]*i)%MOD
            
        return (fac[x+y]*pow(fac[x],MOD-2,MOD)*pow(fac[y],MOD-2,MOD))%MOD
        
    ans = 1
    for pr,num in cl:
        ans *= combinations(N-1,num,N+num)
        ans %= MOD
    
    print(ans)
    
if __name__ == "__main__":
    main()
