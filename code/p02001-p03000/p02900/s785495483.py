# coding: utf-8

def greatest_common_divisor(N, M):
    assert N >= M
    while M != 0:
        N, M = M, N%M
    return N

def prime_divisor(N):
    temp = N
    for n in range(2, int(-(-N**0.5//1))+1):
        if temp % n == 0:
            while temp % n == 0:
                temp //= n
            yield n
    if temp != 1:
        yield temp
        

def main():
    a, b = input().split()
    a, b = int(a), int(b)

    if a > b:
        a, b = b, a

    gcd = greatest_common_divisor(b, a)
    pdiv = [pd for pd in prime_divisor(gcd)]
    print(len(pdiv)+1)

main()