move = [[-1, 2], [0, 2], [1, 2],
        [-1, -2], [0, -2], [1, -2],
        [2, 1], [2, 0], [2, -1],
        [-2, 1], [-2, 0], [-2, -1]]

spraing_range = [[-1, 1], [0, 1], [1, 1],
                 [-1, 0], [0, 0], [1, 0],
                 [-1, -1], [0, -1], [1, -1]]


def main():
    while True:
        px, py = map(int, input().split())
        if px is 0 and py is 0:
            break

        n = int(input())
        tmp = list(map(int, input().split()))
        sprinklers_x = tmp[::2]
        sprinklers_y = tmp[1::2]

        fields = make_fields(sprinklers_x, sprinklers_y)
        if bfs(fields, px, py, n):
            print("OK")
        else:
            print("NA")


def make_fields(sprinklers_x, sprinklers_y):
    fields = []
    for x, y in zip(sprinklers_x, sprinklers_y):
        field = [[0] * 10 for _ in range(10)]
        for dx, dy in spraing_range:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx > 9 or ny > 9:
                continue
            field[ny][nx] = 1

        fields.append(field)

    return fields


def bfs(fields, init_px, init_py, n):
    q = [[init_px, init_py, 0]]  # [px, py, count]
    while len(q) is not 0:
        px, py, count = q.pop(0)

        if count is n:
            return True

        for dx, dy in move:
            nx = px + dx
            ny = py + dy
            if nx < 0 or ny < 0 or nx > 9 or ny > 9 or \
                    fields[count][ny][nx] is 0:
                continue

            q.append([nx, ny, count + 1])

    return False


if __name__ == '__main__':
    main()