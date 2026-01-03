import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]

# Greatest Common Divisor(Euclidean algorithm)


def gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x, y = y, r
    return x


def main():
    n, k = input_int_list()
    A = input_int_list()
    A_max = max(A)
    # Aの最大値よりkが大きい場合は不可
    if k > A_max:
        print("IMPOSSIBLE")
        return

    A_gcd = A[0]
    for a in A:
        A_gcd = gcd(A_gcd, a)

    if k % A_gcd == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

    return


if __name__ == "__main__":
    main()
