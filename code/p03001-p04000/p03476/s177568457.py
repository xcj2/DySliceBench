import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def gen_prime_table(last: int, first=2) -> list:
    if last < 1:
        return [False]
    elif last < 2:
        return [False, False]
    primes = []
    table = [True] * (last + 1)
    table[0] = False
    table[1] = False

    for i in range(first, last + 1):
        if table[i]:
            primes.append(i)
            for j in range(i * 2, last + 1, i):
                table[j] = False
    return table


def main():
    q = input_int()
    prime_table = gen_prime_table(10**5 + 1)
    prime_cusum = [0] * (10**5 + 1)
    for i in range(1, 10**5):
        if prime_table[i] and prime_table[(i + 1) // 2]:
            prime_cusum[i] = prime_cusum[i - 1] + 1
        else:
            prime_cusum[i] = prime_cusum[i - 1]

    for _ in range(q):
        l, r = input_int_list()
        print(prime_cusum[r] - prime_cusum[l - 1])

    return


if __name__ == "__main__":
    main()
