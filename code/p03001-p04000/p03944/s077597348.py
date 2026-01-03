# シミュレーション問題

def paint_gt_x(area, threhsold):
    for y in range(len(area)):
        for x in range(len(area[y])):
            if x < threhsold:
                area[y][x] = 1

def paint_lt_x(area, threhsold):
    for y in range(len(area)):
        for x in range(len(area[y])):
            if x > threhsold:
                area[y][x] = 1

def paint_gt_y(area, threhsold):
    for y in range(len(area)):
        for x in range(len(area[y])):
            if y < threhsold:
                area[y][x] = 1

def paint_lt_y(area, threhsold):
    for y in range(len(area)):
        for x in range(len(area[y])):
            if y > threhsold:
                area[y][x] = 1


(w, h, n) = map(int, input().split())

area = []
for _ in range(h):
    area.append([0 for _ in range(w)])

for _ in range(n):
    (x, y, a) = map(int, input().split())
    if 1 == a:
        paint_gt_x(area, x)
    elif 2 == a:
        paint_lt_x(area, x - 1)
    elif 3 == a:
        paint_gt_y(area, y)
    else:
        paint_lt_y(area, y - 1)

count = 0
for row in area:
    for cell in row:
        count += 1 if 0 == cell else 0
print(count)
