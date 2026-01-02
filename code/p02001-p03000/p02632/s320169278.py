import sys
def input():
    return sys.stdin.readline()[:-1]
MOD = 10**9+7
fac = [1 for k in range(2000010)]
inv = [1 for k in range(2000010)]
finv = [1 for k in range(2000010)]
P25 = [1 for k in range(2000010)]
P26 = [1 for k in range(2000010)]
P25[1] = 25
P26[1] = 26
for k in range(2,2000010):
    fac[k] = (fac[k-1]*k)%MOD
    inv[k] = (MOD - inv[MOD%k] * (MOD // k))%MOD
    finv[k] = (finv[k - 1] * inv[k]) % MOD;
    P26[k] = (P26[k-1]*26) % MOD
    P25[k] = (P25[k-1]*25) % MOD

def nCr(n,r):
    return (fac[n]*finv[r]*finv[n-r])%MOD
def main():
    K = int(input())
    S = input()
    ans = 0
    for k in range(K+1):
#        print(k,nCr(K-k+len(S)-1,len(S)-1))
        ans += nCr(K-k+len(S)-1,len(S)-1)*P25[K-k]*P26[k]
        ans %= MOD
    print(ans)
if __name__ == '__main__':
    main()
