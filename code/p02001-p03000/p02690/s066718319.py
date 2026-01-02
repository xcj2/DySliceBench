def divisor(n):
    result = []
    i = 1
    while True:
        if i * i > n:
            break
        if n % i == 0:
            result.append(i)
            if i != int(n / i):
                result.append(int(n / i))
        i += 1
    return result


def calc(a, b):
    return a * a * a * a * a - b * b * b * b * b


MX = 100000

INF = int(MX**6)


def main():
    X = int(input())
    drs = divisor(X)
    for dr in drs:
        right = MX - dr
        left = -MX
        while right - left > 8:
            bp = int(left + (right - left) / 3)
            bq = int(left + 2 * (right - left) / 3)
            cp = calc(bp + dr, bp)
            cq = calc(bq + dr, bq)
            if cp > cq:
                left = bp
            else:
                right = bq

        mn = INF
        mnb = -2 * MX
        for bi in range(left - 64, right + 64):
            c = calc(bi + dr, bi)
            if mn > c:
                mnb = bi
                mn = c

        left = mnb
        right = MX - dr
        while left <= right:
            b = int((left + right) / 2)
            c = calc(b + dr, b)
            if c == X:
                print(b + dr, b)
                return
            elif c < X:
                left = b + 1
            else:
                right = b - 1

        left = -MX
        right = mnb
        while left <= right:
            b = int((left + right) / 2)
            c = calc(b + dr, b)
            if c == X:
                print(b + dr, b)
                return
            elif c < X:
                left = b + 1
            else:
                right = b - 1


main()
