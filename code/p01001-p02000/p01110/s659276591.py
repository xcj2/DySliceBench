from operator import add


def fold_right(v, length):
    global white_right
    for i in range(white_right, len(v[0])):
        if not any(list(zip(*v))[i]):
            white_right += 1
            continue
        for j in range(length - 1, -1, -1):
            for yoko in range(len(v)):
                v[yoko][i + j + length] += v[yoko][i + (length - 1 - j)]
                v[yoko][i + (length - 1 - j)] = 0
        return v


def fold_up(v, length):
    global white_up
    for i in range(white_up, -1, -1):
        if not any(v[i]):
            white_up -= 1
            continue
        for j in range(length - 1, -1, -1):
            # print(
            #     "i: {} j: {} length: {} i-j: {} i-j-length: {}".format(
            #         i, j, length, i - (length - 1 - j), i - j - length
            #     )
            # )
            v[i - j - length] = list(
                map(add, v[i - j - length], v[i - (length - 1 - j)])
            )
            v[i - (length - 1 - j)] = [0] * len(v[i - j])
        return v


def cut_cut_cut(v):
    global white_right
    global white_up
    for i in range(len(v) - 1, -1, -1):
        if not any(v[i]):
            continue
        white_up = i
        break
    for i in range(len(v[0])):
        if not any(list(zip(*v))[i]):
            continue
        white_right = i
        break


while True:
    n, m, t, p = map(int, input().split())
    if n == 0 and m == 0 and t == 0 and p == 0:
        break
    origami = [[0] * 500 for _ in range(500)]
    for i in range(m):
        for j in range(n):
            origami[len(origami) - 1 - i][j] = 1
    white_right = 0
    white_up = len(origami) - 1
    # print(*origami, sep="\n")
    for i in range(t):
        d, c = map(int, input().split())
        if d == 1:
            origami = fold_right(origami, c)
        else:
            origami = fold_up(origami, c)
        # print(d, c)
        # print(*origami, sep="\n")

    cut_cut_cut(origami)
    for i in range(p):
        x, y = map(int, input().split())
        print(origami[white_up - y][white_right + x])
