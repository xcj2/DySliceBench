import sys
input = sys.stdin.readline

_a, _b = map(int, input().split())


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def get_divisor(a):
    dvlist = []
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            dvlist.append(i)
            if i != a // i:
                dvlist.append(a // i)

    return sorted(dvlist)


def chker(a, b):
    a, b = min(a, b), max(a, b)
    mindiv = get_divisor(a)
    shdvlist = [item for item in mindiv if b % item == 0]
    if len(shdvlist) < 3:
        print(len(shdvlist))
        return

    slist, shdvlist = [shdvlist[1]], shdvlist[1:]
    for item1 in shdvlist:
        flg = 0
        for item2 in slist:
            if item1 % item2 == 0:
                flg = 1
                break

        if flg == 0:
            slist.append(item1)

    print(len(slist) + 1)


chker(_a, _b)
