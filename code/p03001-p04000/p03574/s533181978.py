#■標準入力ショートカット


def get_next_int():
    return int(float(input()))


def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])


def get_next_str():
    return input()


def get_next_strs(delim=" "):
    return tuple(input().split(delim))


def get_next_by_types(*value_types, delim=" "):
    return tuple([t(x) for t, x in zip(value_types, input().split(delim))])


def isMine(x, y, field):
    return field[y][x] == '#'


def count(H, W, x, y, field):
    diff = [-1, 0, 1]
    count = 0
    for d in diff:
        if x + d >= 0 and x + d < W:
            for d2 in diff:
                if y + d2 >= 0 and y + d2 < H:
                    count += 1 if isMine(x + d, y + d2, field) else 0
    return count


def solve():
    H, W = get_next_ints()
    field = []
    for i in range(H):
        field.append(list(get_next_str()))
    for y, line in enumerate(field):
        for x, cell in enumerate(line):
            if cell == '.':
                field[y][x] = str(count(H, W, x, y, field))
    for line in field:
        print(''.join(line))

solve()