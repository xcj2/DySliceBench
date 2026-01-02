def input_int():
    return(int(input()))

def input_int_list():
    return(list(map(int,input().split())))

def input_int_map():
    return(map(int,input().split()))

def run():
    h, w = input_int_map()
    rows = []

    for _ in range(h):
        rows.append(list(input()))

    for row in range(h):
        for col in range(w):
            replace_space(row, col, rows)

    for row in rows:
        print("".join(map(str, row)))

def replace_space(row: int, col:int, rows: []):

    if rows[row][col] != '.':
        return

    h = len(rows)
    w = len(rows[0])

    nums = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

    bomb_count = 0
    for y_diff, x_diff in nums:
        y = row + y_diff
        x = col + x_diff

        if y >= h or y < 0:
            continue

        if x >= w or x < 0:
            continue

        if rows[y][x] == '#':
            bomb_count += 1

    rows[row][col] = bomb_count

run()

# 1, 2, 3
# 2  3  1

# 1  2

# 1, 2  3, 4
# 2  3  4  1











