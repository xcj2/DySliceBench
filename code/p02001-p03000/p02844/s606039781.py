import bisect as bi


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def f(M, i1, i2, i3):
    M1 = M[i1]
    M2 = M[i2]
    M3 = M[i3]

    if len(M1) == 0 or len(M2) == 0 or len(M3) == 0:
        return False

    front = M[i1][0]

    M2 = M[i2]
    if M2[-1] <= front:
        return False

    index = bi.bisect_right(M2, front)
    second = M2[index]

    return second < M[i3][-1]


def main():
    N = int(input())
    S = input()

    M = {i: [] for i in range(10)}
    for i, s in enumerate(S):
        M[int(s)].append(i)

    res = 0
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                if f(M, i1, i2, i3):
                    res += 1
    print(res)


if __name__ == '__main__':
    main()
