import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def f(b, n):
    S = 0
    while n != 0:
        S += n%b
        n //= b
    return S


def solve():
    """
    87654
    138
    -----
    100

    87654
    45678
    -----
    -1

    """
    n = read_int()
    s = read_int()
    for b in range(2, math.ceil(math.sqrt(n))+1):
        if f(b, n) == s:
            return b
    """
    16

    4
    if b>math.sqrt(n) then n=pb+q, p, q < b
                           s=p+q
    n-s=p*(b-1), b-1 >= p
    """
    if n-s < 0:
        return -1
    if n == s:
        return n+1
    for p in range(math.ceil(math.sqrt(n-s)), 0, -1):
        if (n-s)%p == 0 and f((n-s)//p+1, n) == s:
            return (n-s)//p+1
    return -1


if __name__ == '__main__':
    #print(f(10, 87654))
    #print(f(100, 87654))
    print(solve())
