import random


def main():
    X = int(input())
    for i in range(X, 10 ** 6):
        if is_prime(i) == True:
            print(i)
            break


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 561:
        return False
    if n == 1729:
        return False
    for _ in range(100):
        a = random.randint(2, n - 1)
        if gcd(n, a) != 1:
            return False
        if pow(a, n - 1, n) != 1:
            return False
    return True


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    main()
