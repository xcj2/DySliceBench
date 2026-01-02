import sys

def gcd(a, b):
    """Euclidean Algorithm"""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    input = sys.stdin.readline
    A, B, C, D = map(int, input().split())
    E = lcm(C, D)

    total = B - A + 1
    multi_c = max(0, B // C) - max(0, A // C)
    if A % C == 0:
        multi_c += 1
    multi_d = max(0, B // D) - max(0, A // D)
    if A % D == 0:
        multi_d += 1
    multi_e = max(0, B // E) - max(0, A // E)
    if A % E == 0:
        multi_e += 1
    return total - (multi_c + multi_d - multi_e)


if __name__ == '__main__':
    print(main())
