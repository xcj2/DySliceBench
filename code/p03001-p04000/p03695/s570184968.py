def colormap(rate):
    if 1 <= rate < 400:
        return 0
    elif 400 <= rate < 800:
        return 1
    elif 800 <= rate < 1200:
        return 2
    elif 1200 <= rate < 1600:
        return 3
    elif 1600 <= rate < 2000:
        return 4
    elif 2000 <= rate < 2400:
        return 5
    elif 2400 <= rate < 2800:
        return 6
    elif 2800 <= rate < 3200:
        return 7
    elif 3200 <= rate:
        return -1


def solve():
    N = int(input())
    a = [int(x) for x in input().split()]

    colors = [colormap(x) for x in a]

    import collections
    count = collections.Counter(colors)
    # print(count)

    ncolor = len(count) - (-1 in count)

    nmin = 1 if ncolor == 0 else ncolor
    nmax = ncolor + count[-1]

    print(nmin, nmax)


def main():
    solve()


if __name__ == '__main__':
    main()