import math


def sieve_of_eratosthenes(N):
    prime_list = []
    for i in range(0, N):
        if i * i > N:
            break
        prime_list.append(True)
    prime_list[0] = prime_list[1] = False
    prime = []
    n = len(prime_list)
    for i in range(2, n):
        if prime_list[i]:
            prime.append(i)
            for j in range(2 * i, n, i):
                prime_list[j] = False
    return prime


def cal_count(prime, N):
    for i in range(len(prime)):
        if N < prime[i]:
            break
        while N % prime[i] == 0:
            print('', prime[i], end='')
            N //= prime[i]
    if N != 1:
        print('', N, end='')
    print()


def main():
    N = int(input())
    prime = sieve_of_eratosthenes(N)
    prime.append(N)
    print(N,end='')
    print(':', end='')
    cal_count(prime, N)


if __name__ == '__main__':
    main()

