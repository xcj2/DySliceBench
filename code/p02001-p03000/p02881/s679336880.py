def p_a():
    A, B = map(int, input().split())
    print(A * B if A < 10 and B < 10 else -1)


def p_b():
    N = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if N == i * j:
                print("Yes")
                exit()
    print("No")


import math


def p_c():
    N = int(input())
    m = int(math.sqrt(N))

    for i in reversed(range(1, m + 1)):
        if N % i == 0:
            print(i + N // i - 2)
            break


def p_d():
    pass


def p_e():
    pass


def p_f():
    pass


if __name__ == '__main__':
    p_c()
