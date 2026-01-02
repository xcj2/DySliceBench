n = int(input())
k = int(input())

fact = [1]
for i in range(1, 101):
    fact += [fact[i-1] * i]


def nCk(N, K):
    if K > n or K < 0:
        return 0
    return fact[N] // fact[K] // fact[N-K]


def digits(N):
    N = abs(N)
    ret = 0
    x = 1
    while x <= N:
        ret += 1
        x *= 10
    return ret

def solve(N, K):
    if K == 0 and N == 0:
        return 1
    if K == 0 and N > 0:
        return 1
    if K > 0 and N == 0:
        return 0

    d = digits(N)
    if d < K:
        return 0

    top = N // (10**(d-1))
    return (top-1) * 9**(K-1) * nCk(d-1,K-1) + 9**(K) * nCk(d-1,K) + solve(N % (10**(d-1)), K-1)

print(solve(n,k))