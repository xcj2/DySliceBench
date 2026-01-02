def find_min(v):
    x = v % 10
    return (x % 5, x//5, v // 10)

def find_max(v):
    return (v, 0, 0)


def conv10to5(xs):
    return (xs[0], xs[1] +2, xs[2] - 1)

def undoconv10to5(xs):
    return (xs[0], xs[1] -2, xs[2] + 1)


def conv5to1(xs):
    return (xs[0]+5, xs[1] -1, xs[2])


def next(xs):
    if xs[2] == 0:
        if xs[1] == 0:
            return None
        else:
            return conv5to1(xs)
    else:
        if xs[1] < 7:
            return conv10to5(xs)
        else:
            return conv5to1(undoconv10to5(undoconv10to5(undoconv10to5(xs))))


def find(v, n):
    xs = find_min(v)
    m = sum(xs)
    if m > n or n > v:
        return (-1, -1, -1)

    while xs:
        if sum(xs) == n:
            return xs
        xs = next(xs)
    return (-1, -1, -1)



if __name__ == "__main__":
    n, y = map(int, input().split())
    y = y // 1000
    print("{2} {1} {0}".format(*find(y, n)))
    