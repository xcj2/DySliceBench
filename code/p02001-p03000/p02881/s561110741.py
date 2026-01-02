import math


def solve():
    n = read()
    result = think(n)
    write(result)


def read():
    return read_int(1)[0]


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(n):
    """
    >>> think(10)
    5
    >>> think(50)
    13
    >>> think(10000000019)
    10000000018
    """

    if is_prime(n):
        return n - 1  # from (1, 1) to (1, n) is the least. so distance is (n - 1)
    ceil = int(math.ceil(math.sqrt(n)))
    for a in range(ceil, -1, -1):
        if n % a == 0:
            b = n // a
            return (a - 1) + (b - 1)  # from (1, 1) to (a, b) is the least. so distance is (a - 1) + (b - 1)


def write(result):
    print(result)


def is_prime(n):
    """
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    >>> is_prime(14)
    False
    >>> is_prime(15)
    False
    >>> is_prime(16)
    False
    >>> is_prime(17)
    True
    >>> is_prime(18)
    False
    >>> is_prime(19)
    True
    >>> is_prime(20)
    False
    >>> is_prime(23)
    True
    >>> is_prime(25)
    False
    >>> is_prime(29)
    True
    >>> is_prime(30)
    False
    >>> is_prime(31)
    True
    """

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    ceil = int(math.ceil(math.sqrt(n))) + 1
    for x in range(3, ceil, 2):
        if n == x:
            return True
        else:
            if n % x == 0:
                return False
    return True


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    solve()