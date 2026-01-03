import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def digits(n):
    count = 1
    while n > 9:
        n //= 10
        count += 1
    return count


def solve():
    N = read_int()
    low, high = 0, 10**5+1
    while high-low > 1:
        mid = low+(high-low)//2
        if mid*mid > N:
            high = mid
        else:
            low = mid
    min_f = math.inf
    for i in range(1, low+1):
        if N%i == 0:
            min_f = min(min_f, max(digits(i), digits(N//i)))
    return min_f


if __name__ == '__main__':
    print(solve())
