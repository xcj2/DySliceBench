import sys
input = sys.stdin.readline
import numpy as np
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
def calc(x, C, D, l):
    x1 = x // C
    x2 = x // D
    x3 = x // l
    return x - x1 -x2 + x3

def print_ans(A, B, C, D):
    """Test Case
    >>> print_ans(4, 9, 2, 3)
    2
    >>> print_ans(10, 40, 6, 8)
    23
    >>> print_ans(314159265358979323, 846264338327950288, 419716939, 937510582)
    532105071133627368
    """
    # Greatest common divisor
    g = gcd(max(C,D),min(C,D))
    # Least common multiple
    l = C * D // g
    print(calc(B, C, D, l) - calc(A - 1, C, D, l))



if __name__ == '__main__':
    A, B, C, D = map(int, input().rstrip().split())
    print_ans(A, B, C, D)


