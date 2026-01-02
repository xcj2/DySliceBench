def main():
    n = iread()
    h = aread()
    cnt = 0
    i = 0
    while i < n:
        tmpcnt = 0
        while i + 1 < n and h[i + 1] <= h[i]:
            tmpcnt += 1
            i += 1
        i += 1
        cnt = max(tmpcnt, cnt)
    print(cnt)


def iread():
    return int(input())


def sread():
    return input()


def aread(t="int"):
    if t == "int":
        ret = [int(i) for i in input().split()]
    elif t == "str":
        ret = list(input())
    return ret


def scan():
    return list(map(int, input().split()))


if __name__ == '__main__':
    main()
