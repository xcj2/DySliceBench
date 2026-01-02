import bisect


def calc(X, Y):
    dic = dict([(X * (2**x), x) for x in range(80)])
    ret = bisect.bisect(list(dic.keys()), Y)

    return ret


def calc2(X, Y):
    cnt = 0
    tmp = X
    while tmp <= Y:
        tmp *= 2
        cnt += 1
    return cnt


def main():
    X, Y = list(map(int, input().split()))
    print(calc2(X, Y))
    # print(calc(X, Y))


if __name__ == '__main__':
    main()
    # import random
    # for i in range(3000000):
    #     x = random.randint(1, 1000000000000000000)
    #     y = random.randint(x, 1000000000000000000)
    #     if (calc(x, y) != calc2(x, y)):
    #         print(x, y)
