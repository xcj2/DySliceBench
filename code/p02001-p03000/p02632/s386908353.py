import sys

def input():
    return sys.stdin.readline().strip()

def main():
    K = int(input())
    S = input()

    mod = 10 ** 9 + 7
    n = len(S)
    ans = 0

    fact =[1]*(K+n)
    factinv = [1]*(K+n)
    inv = [0,1]


    for i in range(2,K+n):
        fact[i] = (fact[i-1] * i) % mod
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv[i] = (factinv[i-1] * inv[i]) % mod

    def nCr(n,r):
        r = min(r,n-r)
        return (fact[n] * factinv[r] * factinv[n-r]) % mod

    for i in range(K+1):
        tmp = pow(25,i,mod)
        tmp *= nCr(i+n-1,n-1)
        tmp *= pow(26,K-i,mod)
        ans += tmp
        ans %= mod
    print(ans)

if __name__ == "__main__":
    main()