import sys

def input():
    return sys.stdin.readline().strip()


def main():
    def make_factorial_table(n):
        result = [0] * (n+1)
        result[0] = 1
        for i in range(1,n+1):
            result[i] = result[i-1] * i % mod
        return result
    
    def nCr(n,r):
        return fact[n] * pow(fact[n-r],mod-2,mod) * pow(fact[r],mod-2,mod) % mod

    K = int(input())
    S = input()
 
    mod = 10 ** 9 + 7
    n = len(S)
    ans = 0
    fact = make_factorial_table(n+K+1)

    for i in range(K+1):
        tmp = pow(25,i,mod)
        tmp *= nCr(i+n-1,n-1)
        tmp *= pow(26,K-i,mod)
        ans += tmp
        ans %= mod
    print(ans)
 
if __name__ == "__main__":
    main()