import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    if N == 1:
        return 0
    max_divisor = math.sqrt(N)
    divisor = 2
    counter = 0
    while divisor <= max_divisor:
        temp_divisor = divisor
        while N%temp_divisor == 0:
            N //= temp_divisor
            temp_divisor *= divisor
            counter += 1
        while N%divisor == 0:
            N //= divisor
        divisor += 1
    if N != 1:
        counter += 1
    return counter


if __name__ == '__main__':
    print(solve())
