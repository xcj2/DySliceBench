
def read_input():
    n = int(input())
    alist = list(map(int, input().split()))

    return n, alist

def get_rate(x):
    if x < 400:
        return 1
    elif x < 800:
        return 2
    elif x < 1200:
        return 3
    elif x < 1600:
        return 4
    elif x < 2000:
        return 5
    elif x < 2400:
        return 6
    elif x < 2800:
        return 7
    elif x < 3200:
        return 8
    else:
        return 9

def submit():
    n, alist = read_input()
    rates = [get_rate(a) for a in alist]

    colors = {}
    for r in rates:
        if r == 9:
            continue

        if r not in colors.keys():
            colors[r] = 1
        else:
            colors[r] += 1

    tops = [r for r in rates if r == 9]
    color_n = len(colors)

    if color_n == 0:
        # minではtopは1色に合わせる
        color_min = 1
        color_max = len(tops)
    else:
        # minではtopは既存に色を合わせる
        color_min = color_n
        color_max = color_n + len(tops)

    print('{} {}'.format(color_min, color_max))


if __name__ == '__main__':
    submit()