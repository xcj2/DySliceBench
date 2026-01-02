def f1(a, b, c, d):  # 2点の中心を通り垂直な線の傾きと切片
    k = (a - c) / (d - b)
    h = ((b + d) - k * (a + c)) / 2
    return k, h


def f2(a, b, c, d):  # 2直線との交点
    x = (d - b) / (a - c)
    y = a * x + b

    return x, y


def f3(a, b, c, d):
    return ((c - a) ** 2 + (d - b) ** 2) ** 0.5


def main():
    N = int(input())
    for i in range(N):
        a, b, c, d, e, f = map(float, input().split())
        T = []
        if not b == d:
            k, h = f1(a, b, c, d)
            T.append((k, h))
        if not d == f:
            k, h = f1(c, d, e, f)
            T.append((k, h))
        if not  f == b:
            k, h = f1(e, f, a, b)
            T.append((k, h))
        x, y = f2(T[0][0], T[0][1], T[1][0], T[1][1])
        r = f3(x, y, a, b)
        print(f'{round(x, 3):.3f} {round(y, 3):.3f} {round(r, 3):.3f}')


if __name__ == '__main__':
    main()

