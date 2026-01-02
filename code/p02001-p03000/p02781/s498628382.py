from math import factorial


def nCr(n, r):
    if r <= 0:
        return 0

    if n >= r:
        return factorial(n) // (factorial(n - r) * factorial(r))
    else:
        return 0

def main():
    N = input()
    K = int(input())

    ans = func(N, K)

    print(ans)

def func(N, K):
    N = N.lstrip('0')
    if len(N) < K:
        return 0

    if K == 0:
        return 1

    n = int(N[0])

    if len(N) == 1:
        if K > 1:
            return 0
        else:
            return n

    ret = 0
    if K > 1:
        ret += func(N[1:], K-1)
    else:
        ret += 1
    l = len(N[1:])

    ret += (n - 1) * func('9' * l, K - 1)
    if l >= K:
        ret += func('9'* l, K)

    # ret += (n - 1) * nCr(l-1, K - 2) * 9 ** (K - 1)
    # ret += nCr(l-1, K - 1) * 9 ** K 

    return ret
    

if __name__ == '__main__':
    main()