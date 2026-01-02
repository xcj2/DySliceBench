# -*- coding: utf-8 -*-


def main():
    A, B = [int(_) for _ in input().split()]

    product = A * B
    for divisor in range(min([A, B]) // 2, 2, -1):
        if A % divisor == 0 and B % divisor == 0:
            A = A // divisor
            B = B // divisor
            product = product // divisor

    print(product)


def correct_1():
    A, B = [int(_) for _ in input().split()]

    for i in range(1, B + 1):
        if A * i % B == 0:
            print(A * i)
            break


def correct_2():
    A, B = [int(_) for _ in input().split()]

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    print(lcm(A, B))


if __name__ == "__main__":
    correct_2()
