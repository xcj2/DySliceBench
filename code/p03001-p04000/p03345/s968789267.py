def main():
    A, B, C, K = map(int, input().split())

    # TLE(A, B, C, K)
    f(A, B, C, K)


def f(A, B, C, K):
    """
    1: (A,B,C) = (    B  C,  A     C,  A  B   )
    2: (A,B,C) = (2A  B  C,  A 2B  C,  A  B 2C)
    3: (A,B,C) = (2A 3B 3C, 3A 2B 3C, 3A 3B 2C)
    4: (A,B,C) = (6A 5B 5C, 5A 6B 5C, 5A 5B 6C)
    """
    if A == B == C:
        print(0)
        return

    ans = int((B - A) * (-1) ** (K - 1))
    if abs(ans) > 10 ** 18:
        print("Unfair")
    else:
        print(ans)


def TLE(A, B, C, K):
    for i in range(K):
        bc = B + C
        ab = A + B
        ac = A + C
        print(A, B, C, bc, ab, ac, sep="\t")
        A = bc
        B = ac
        C = ab

    ans = A - B
    if abs(ans) > 10 ** 18:
        print("Unfair")
    else:
        print(ans)


if __name__ == '__main__':
    main()
