from collections import OrderedDict
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
def factorize(m):
    d = []
    for i in range(1, int(m**0.5)+1):
        if m % i == 0:
            d.append(i)
            if i != m // i:
                d.append(m//i)
    return d
def main():
    N = int(input())
    A = list(map(int, input().split()))
    l = list(set(factorize(A[0]) + factorize(A[1])))
    l.sort(reverse=True)
    d = OrderedDict()
    for i in l:
    	d[i] = 0
    for i in A:
        for j in d:
            if i % j == 0:
                d[j] += 1
    m = 1
    for k in d:
        if d[k] >= N-1:
            print(k)
            return
    print(1)
main()
