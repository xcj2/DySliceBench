import sys
input = sys.stdin.readline

MOD = 10**9+7
fact = []
memo = {}

def pow(a):
    b = MOD-2
    res = 1
    while b:
        if b & 1: res = res * a % MOD
        a = a**2 % MOD
        b >>= 1
    return res

def comb(n, r):
    global fact, memo
    if r < 0 or r > n: return 0
    if r in memo: a = memo[r]
    else: a = memo[r] = pow(fact[r])

    if n-r in memo: b = memo[n-r]
    else: b = memo[n-r] = pow(fact[n-r])
    
    return (fact[n] * a) % MOD * b % MOD 

def main():
    global fact, memo
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))

    fact = [1] * (N+1)
    
    for i in range(2, N+1): fact[i] = fact[i-1] * i % MOD    
    ans = 0

    for i in range(2):
        for j in range(N):
            n = comb(j, K-1)
            if i == 1: n = -n
            ans += n * A[j]
        if i == 0: A.reverse()
    print(ans%MOD) 

if __name__ == '__main__':
    main()