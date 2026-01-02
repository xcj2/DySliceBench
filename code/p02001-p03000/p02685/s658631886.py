import sys
sys.setrecursionlimit(100000000)
MOD = 998244353
INF = 10 ** 15

MAXN = 200005
factorial = [1]
for i in range(1, MAXN + 1):
    factorial.append(factorial[-1] * i % MOD)

inv_factorial = [-1] * (MAXN + 1)
inv_factorial[-1] = pow(factorial[-1], MOD-2, MOD)
for i in reversed(range(MAXN)):
    inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

def fact(n):
    return factorial[n]%MOD

def nck(n, k):
    if k>n or k<0:
        return 0
    else:
        return factorial[n]*inv_factorial[n - k]*inv_factorial[k]%MOD

def main():  
    N,M,K = map(int,input().split())
    invs = [1]
    for i in range(N + 1):
        invs.append(invs[-1]*pow(M,MOD - 2,MOD)%MOD)

    ans = 0
    for i in range(K + 1):
        ret = nck(N - 1,i)*invs[i]%MOD
        ret *= invs[N - i - 1]*pow(M - 1,N - i - 1,MOD)%MOD
        ans += ret%MOD
        ans %= MOD
    ans *= pow(M,N,MOD)
    ans %= MOD
    print(ans)
if __name__ == '__main__':
    main()