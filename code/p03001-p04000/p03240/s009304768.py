#!/usr/bin/env pypy3


def get_line():
    return input()


def get_tokens():
    return get_line().split()


def get_ints():
    return [int(_) for _ in get_tokens()]


def main():
    n, = get_ints()

    inp = [get_ints() for _ in range(n)]
    x, y, h = zip(*inp)

    def calc(cx, cy):
        low = 1
        high = max(h) + 2000

        for x_, y_, h_ in zip(x, y, h):
            if h_ > 0:
                H = abs(cx - x_) + abs(cy - y_) + h_
                if low <= H <= high:
                    low = high = H
                else:
                    return None
            else:
                H = abs(cx - x_) + abs(cy - y_) + h_
                high = min(high, H)
                if low > high:
                    return None
                    
        if low == high:
            return low
        else:
            return None

    for cx in range(101):
        for cy in range(101):
            ans = calc(cx, cy)
            if ans is not None:
                print(cx, cy, ans)
                return
    assert False


if __name__ == '__main__':
    main()