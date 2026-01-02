MOD = 10**9 + 7

def mul(a, b):
    return [
        [sum(aij * bij for aij, bij in zip(ai, bi)) % MOD for bi in zip(*b)]
        for ai in a]

def pow(b, k):
    r = [[1 if i == j else 0 for i in range(len(b))] for j in range(len(b))]
    while k:
        if k & 1:
            r = mul(r, b)
        k >>= 1
        b = mul(b, b)
    return r


def main():
    N, K = (int(i) for i in input().split())
    A = []
    for i in range(N):
        A.append([int(j) for j in input().split()])
    A = [i for i in zip(*A)]
    v = [[1] * N]
    return sum(mul(v, pow(A, K))[0]) % MOD

print(main())
