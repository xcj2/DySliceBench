from collections import defaultdict


def combination(n, r):
    ret = 1
    a = 1
    b = 1
    for i in range(1,r+1):
        a *= (n+i-1)
        b *= (r-i+1)
    return a // b


def compute_divisors(n):
    ret = defaultdict(int)
    m = n
    while m%2 == 0:
        ret[2] += 1
        m = m//2
    r = 3
    while m > 1:
        if r**2 > m:
            ret[m] = 1
            break
        while m%r==0:
            ret[r] += 1
            m = m//r
        r += 2
    return ret


def main():
    N, M = list(map(int, input().split(' ')))
    divisors = compute_divisors(M)
    exp = 0
    ret = 1
    for d in divisors:
        c = divisors[d]
        ret *= combination(N,c)
        ret %= 1000000007
    print(ret)


if __name__ == '__main__':
    main()