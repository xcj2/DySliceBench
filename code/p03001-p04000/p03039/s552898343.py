import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M,K=MI()
    #2この組み合わせを全部足して，平均ぽく考える
    
    def sum2(x):
        return ((x*(x+1))//2)%mod
    
    #i,jますにいるときの相手．（i,j）よりも奥にあるやつの全組み合わせの総和
    def calc(i,j):
        temp=0
        temp=sum2(M-j-1)#該当する行
        temp=(temp+((sum2(M-j-1)+sum2(j))*(N-i-1)))%mod#下の行の階差部分，左右方向にあるから
        temp=(temp+sum2(N-i-1)*M)%mod
        return temp
        
    S=0
    for i in range(N):
        for j in range(M):
            S=(S+calc(i,j))%mod
            
    rem=(N*M)-2
    
    def cmb(n, r, mod):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return (fact[n] * factinv[r] * factinv[n-r])%mod

    fact=[1,1]
    factinv=[1,1]
    inv=[0,1]
    
    for i in range(2, rem + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)  
        
    #print(rem,K-2)
    S=(S*cmb(rem,K-2,mod))%mod
            
    print(S)

main()
