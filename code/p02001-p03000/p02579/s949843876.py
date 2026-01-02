h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())

s = list()
offsets = list()

for i in range(-2, 3):
    for j in range(-2, 3):
        offsets.append((i, j))


def print_map(m):
    for mm in m:
        print(mm)


def label(num, x, y):
    res = list()
    if not (0 <= x < h and 0 <= y < w):
        return res
    if s[x][y] != ".":
        return res
    s[x][y] = num

    res += label(num, x - 1, y)
    res += label(num, x + 1, y)
    res += label(num, x, y - 1)
    res += label(num, x, y + 1)

    res.append((x, y))

    return res


def find_next(x, y):
    res = list()

    for offset in offsets:
        xx, yy = x + offset[0], y + offset[1]
        if not (0 <= xx < h and 0 <= yy < w):
            continue

        if s[xx][yy] == ".":
            res.append((xx, yy))

    return res


for i in range(h):
    s.append(list(input()))

stage = 0
labeled = label(stage, dh - 1, dw - 1)

stage += 1

while len(labeled) > 0:
    new_labeled = list()
    for l in labeled:
        nexts = find_next(l[0], l[1])
        for n in nexts:
            new_labeled += label(stage, n[0], n[1])

    labeled = new_labeled
    stage += 1

if s[ch - 1][cw - 1] != ".":
    print(s[ch - 1][cw - 1])
else:
    print(-1)
