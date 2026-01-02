import math
import itertools
import sys

prime_numbers = set()
table = [0 for i in range(10 ** 5 + 1)]
input = lambda: sys.stdin.readline().strip()


def is_primenumber(x):
    if x in prime_numbers:
        return True
    if x == 1:
        return False
    elif x == 2:
        prime_numbers.add(2)
        return True
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        prime_numbers.add(x)
        return True


def is_like_2017(x):
    return is_primenumber(x) and is_primenumber((x + 1) // 2)


def query(l, r):
    print(table[r] - table[l - 1])


if __name__ == "__main__":
    for i in range(1, 10 ** 5 + 1, 2):
        if is_like_2017(i):
            table[i] += 1
    table = [x for x in itertools.accumulate(table)]
    Q = int(input())

    for _ in range(Q):
        l, r = [int(x) for x in input().split(" ")]
        query(l, r)
