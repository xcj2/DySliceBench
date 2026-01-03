def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def cumsum(a):
    c= [0] * len(a)
    c[0] = a[0]
    for i in range(1, len(a)):
        c[i] = a[i] + c[i-1]
    return c


def calc(a, signs):
    s = cumsum(a)

    op = 0
    ans = 0
    for i, sig in enumerate(signs):
        s[i] = s[i] + op
        mysign = sign(s[i])

        if mysign != sig:
            delta = sig*(abs(s[i]) + 1)
            op += delta
            s[i] += delta
            ans += abs(delta)
    return ans


def solve():
    N = int(input())
    a = [int(x) for x in input().split()]

    signs1 = [1] * N
    for i in range(N):
        if i%2==0:
            signs1[i] = -1
    signs2 = list(map(lambda x: -x, signs1))

    return min(calc(a, signs1), calc(a, signs2))


def main():
    print(solve())


if __name__ == '__main__':
    main()