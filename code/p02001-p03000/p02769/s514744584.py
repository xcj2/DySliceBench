def main():
    n,k=map(int,input().split())
    mod=10**9+7

    import numpy as np
    def prepare(n):
        nrt = int(n ** 0.5) + 1
        nsq = nrt * nrt
        facts = np.arange(nsq, dtype=np.int64).reshape(nrt, nrt)
        facts[0, 0] = 1
        for i in range(1, nrt):
            facts[:, i] = facts[:, i] * facts[:, i - 1] % mod
        for i in range(1, nrt):
            facts[i] = facts[i] * facts[i - 1, -1] % mod
        facts = facts.ravel().tolist()
 
        invs = np.arange(1, nsq + 1, dtype=np.int64).reshape(nrt, nrt)
        invs[-1, -1] = pow(facts[-1], mod - 2, mod)
        for i in range(nrt - 2, -1, -1):
            invs[:, i] = invs[:, i] * invs[:, i + 1] % mod
        for i in range(nrt - 2, -1, -1):
            invs[i] = invs[i] * invs[i + 1, 0] % mod
        invs = invs.ravel().tolist()
 
        return facts, invs

    facts,invs=prepare(3*n)
    
    def nck(n,k):
        if k<0 or k>n:
            return 0
        else:
            return facts[n]*invs[n-k]*invs[k]%mod

    if k>=n-1:
        print(nck(2*n-1,n-1))
        exit()
    
    else:
        ans=0
        for i in range(k+1):
            ans+=nck(n,i)*nck(n-1,i)
            ans%=mod
        print(ans)
if __name__=='__main__':
    main()