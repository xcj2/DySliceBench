import math


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    T1, T2 = read_values()
    A1, A2 = read_values()
    B1, B2 = read_values()

    if A1 * T1 + A2 * T2 == B1 * T1 + B2 * T2:
        print("infinity")
        return

    D1 = (A1 - B1) * T1
    D2 = (A2 - B2) * T2

    if D1 * D2 > 0:
        print(0)
        return

    D1 = abs(D1)
    D2 = abs(D2)

    if D1 > D2:
        print(0)
        return

    i = D1 // (D2 - D1)
    if D1 == i * (D2 - D1):
        print(i * 2)
    else:
        print(1 + 2 * i)


if __name__ == '__main__':
    main()
