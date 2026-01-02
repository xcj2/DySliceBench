import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    X,Y=MI()
    N3=X+Y
    
    if N3%3!=0:
        print(0)
        exit()
        
    N=N3//3
    a=0
    b=0
    for i in range(N+1):
        if 2*i + (N-i) == X:
            a=i
            b=N-i
            break
        
    if a==0 and b==0:
        print(0)
        exit()

    fact=[1,1]
    factinv=[1,1]
    inv=[0,1]

    for i in range(2, N + 5):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
        
    ans=fact[N]*factinv[a]*factinv[b]
    print(ans%mod)
    

main()
