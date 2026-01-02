#!/usr/bin/env pypy3


def get_line():
    return input()


def get_tokens():
    return get_line().split()


def get_ints():
    return [int(_) for _ in get_tokens()]


def main():
    n, m = get_ints()

    divs = []

    div = 1
    while div * div <= m:
        if m % div == 0:
            divs.append(div)
            if div * div < m:
                divs.append(m // div)
        div += 1
        
    divs.sort()
    ratios = [m // div for div in divs]

    i = 0
    while i + 1 < len(divs) and ratios[i + 1] >= n:
        i += 1
    print(divs[i])


if __name__ == '__main__':
    main()