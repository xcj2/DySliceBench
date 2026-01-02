#!/usr/bin/env pypy3


def get_line():
    return input()


def get_tokens():
    return get_line().split()


def get_ints():
    return [int(_) for _ in get_tokens()]


def main():
    n, = get_ints()
    w = []
    for i in range(n):
        v = get_line()
        w.append(v)

    s = set()
    ok = True
    s.add(w[0])
    last_v = w[0]
    for i in range(1, n):
        v = w[i]
        if v[0] != last_v[-1]:
            ok = False
        if v in s:
            ok = False
        s.add(v)
        last_v = v

    print('Yes' if ok else 'No')


if __name__ == '__main__':
    main()