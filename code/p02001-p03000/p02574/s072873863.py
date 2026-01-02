import math


def simple_sol(N, A):
    is_pairwise_coprime = True
    for i in range(N - 1):
        for j in range(i + 1, N):
            g = math.gcd(A[i], A[j])
            if g == 1:
                continue
            is_pairwise_coprime = False
            break
        if not is_pairwise_coprime:
            break
    if is_pairwise_coprime:
        return 'pairwise coprime'
    g = A[0]
    for i in range(1, N):
        g = math.gcd(g, A[i])
        if g == 1:
            return 'setwise coprime'
    return 'not coprime'



def factorial(n): 
    f = []
    c = 0
    r = int(n**0.5)
    for i in range(2, r + 2):
        while n % i == 0:
            c += 1
            n = n // i
        if c !=0 :
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f


def main():
    N = int(input())
    A = list(map(int, input().split()))
    # print(simple_sol(N, A))
    exponents = [0] *  (10 ** 6 + 1)
    is_pairwise_coprime = True
    for a in A:
        for x, e in factorial(a):
            if exponents[x] > 0:
                is_pairwise_coprime = False
                break
            exponents[x] = e
        if not is_pairwise_coprime:
            break
    if is_pairwise_coprime:
        print('pairwise coprime')
        return
    g = A[0]
    for i in range(1, N):
        g = math.gcd(g, A[i])
        if g == 1:
            print('setwise coprime')
            return
    print('not coprime')


if __name__ == '__main__':
    main()
