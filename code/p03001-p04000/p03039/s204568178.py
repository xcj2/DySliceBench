import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    """
    まず，xとyを分離する=>xだけを考えるので1行とみなす．
    いっぺんにいくつも考えられないので，コマを2つだけ置いた時を考える．
    2この組み合わせで距離が1=>M-1通り，2=>M-2通り,...,M-1=>1通り
    (以下のように考えてΣしても良いがやや面倒
        (j列目にコマを固定すると，相手との距離はj,j-1,...,1,0,1,2,...,M-j))
    実際にはN列あるので，選び方がN^2
        同じ行・列を選んだ場合は不可能だけど，どうせ距離も0なので関係ない
        
    ある2つの組みに注目した時，それを何回数えるかは，外野の並べ方に依存
    (N*M-2)C(K-2)通り
    """
    N,M,K=MI()
    
    
    def cmb(n, r, mod):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return (fact[n] * factinv[r] * factinv[n-r])%mod

    fact=[1,1]
    factinv=[1,1]
    inv=[0,1]
    
    for i in range(2, N*M+5+ 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
    
    tempj=0
    for j in range(M):
        tempj+=(M-j)*j
        
    tempi=0
    for i in range(N):
        tempi+=(N-i)*i

        
    ans=(tempj*N*N)%mod
    ans=(ans+tempi*M*M)%mod
    ans=(ans*cmb(N*M-2,K-2,mod))%mod
    
    print(ans)
    

main()
