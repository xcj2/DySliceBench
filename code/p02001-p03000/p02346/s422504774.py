def add(bit, a, w, n):
    x = a
    while x <= n:
        bit[x] += w
        x += x & -x


def sum_from_zero(bit, a):
    ret = 0
    x = a
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret


def main():
    [n, q] = [int(num) for num in input().split()]

    bit = [0 for _ in range(n + 1)]

    for i in range(q):
        [com, x, y] = [int(num) for num in input().split()]

        if com == 0:
            add(bit, x, y, n)
        else:
            print(sum_from_zero(bit, y) - sum_from_zero(bit, x-1))


if __name__ == '__main__':
    main()

