def read(): return list(map(int, input().split()))


def calc(h, w):
    S = h * w

    ret = 1145141919
    for x in range(1, w + 1):
        s1 = h * x
        if h % 2 == 0:
            s2 = (h // 2) * (w - x)
        elif (w - x) % 2 == 0:
            s2 = ((w - x) // 2) * h
        else:
            t2 = h * ((w - x) // 2)
            t3 = S - s1 - t2

            s2 = (w - x) * (h // 2)
            s3 = S - s1 - s2

            ret = min(ret, max(s1, t2, t3) - min(s1, t2, t3), max(s1, s2, s3) - min(s1, s2, s3))
            continue

        s3 = S - s1 - s2

        smax = max(s1, s2, s3)
        smin = min(s1, s2, s3)

        ret = min(ret, smax - smin)

    return ret


def main():
    h, w = read()
    if h % 3 == 0 or w % 3 == 0:
        print(0)
        return

    ans = calc(h, w)
    h, w = w, h
    ans = min(ans, calc(h, w))
    print(ans)


if __name__ == '__main__':
    main()