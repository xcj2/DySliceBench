import math

def fact(N):
    total = 1
    for i in range(1, N+1):
        total = total * i
    return total

def comb(a, b):
    return fact(a) // (fact(a-b) * fact(b))


def main():
    N, K = list(map(int, input().split(" ")))
    a = N - K + 1
    b = 1
    mod = 1000000007
    ans = ((a % mod) * (b % mod)) % mod
    print(ans)
    for i in range(1, K):
        tmp_a = (N-K+1-i)
        if tmp_a == 0:
            tmp_a = 1
        tmp_b = (K-1-i+1)
        if tmp_b == 0:
            tmp_b = 1
        a = (a * tmp_a) // (i+1)
        b = (b * tmp_b) // i
        ans = ((a % mod) * (b % mod)) % mod
        print(ans)

if __name__ == '__main__':
    main()
