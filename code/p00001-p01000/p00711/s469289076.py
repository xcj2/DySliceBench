def location(field, wanted):
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            if cell == wanted:
                return i, j
def count(field, wanted):
    result = 0
    for row in field:
        for cell in row:
            if cell == wanted:
                result += 1
    return result
def neighborhood(center, w, h):
    i, j = center
    return filter(lambda x: 0 <= x[0] and x[0] < h and 0 <= x[1] and x[1] < w,
                  [                (i - 1, j    ),
                   (i    , j - 1),                 (i    , j + 1),
                                   (i + 1, j    )])
printed_later = []
while True:
    #入力
    w, h = map(int, input().split())
    if(w == 0 and h == 0):
        break
    field = []  # strの配列すなわちcharの配列の配列 '.':黒 '#':赤 '@':スタート (',':到達可能)
    for i in range(h):
        field.append(list(input()))
    #出力　幅優先探索
    queue = [location(field,'@')]
    field[queue[0][0]][queue[0][1]] = ','
    while len(queue) > 0:
        for cell in neighborhood(queue.pop(0), w, h):
            if field[cell[0]][cell[1]] == '.':
                queue.append(cell)
                field[cell[0]][cell[1]] = ','
    printed_later.append(count(field, ','))
for line in printed_later:
    print(line)
