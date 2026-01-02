h, w = map(int, input().split())

def conv_e_2_num(x):
    return 1 if x == "#" else 0

def is_painted(masu, x, y):
    return masu[y][x] == 1

def check_lrtb(masu, x, y, w, h):
    return (x - 1 >= 0 and is_painted(masu, x - 1, y)) \
        or (x + 1 < w and is_painted(masu, x + 1, y)) \
        or (y - 1 >= 0 and is_painted(masu, x, y - 1)) \
        or (y + 1 < h and is_painted(masu, x, y + 1)) \

def check_all(masu, w, h):
    if w == h and w == 1:
        return True
    for y in range(h):
        for x in range(w):
            if is_painted(masu, x, y):
                if check_lrtb(masu, x, y, w, h):
                    continue
                else:
                    return False
    return True


masu = []
for y in range(h):
    masu.append(list(map(conv_e_2_num, list(input()))))

print('Yes') if check_all(masu, w, h) else print('No')
