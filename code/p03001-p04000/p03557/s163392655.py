N = int(input())

An = sorted([int(i) for i in input().split()])
Bn = map(int, input().split())
Cn = sorted([int(i) for i in input().split()])


def lowerBound(a, v):
    # 以上
    return lb(a, 0, len(a), v)


def upperBound(a, v):
    # より大きい
    # 値をプラス1
    return lb(a, 0, len(a), v + 1)


def lb(a, l, r, v):
    low = l - 1
    high = r

    while high - low > 1:
        mid = low + high >> 1
        if a[mid] >= v:
            high = mid
        else:
            low = mid

    return high


def main():
    print(sum([lowerBound(An, Bi)
               * (N - upperBound(Cn, Bi)) for Bi in Bn]))

    return


main()
