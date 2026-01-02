import copy

MOVEMENT = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def main():
    H, W = [int(s) for s in input().split()]
    MAP = []
    for h in range(H):
        row = input()
        MAP.append(list(row))

    points = []
    for h in range(H):
        for w in range(W):
            if MAP[h][w] == '.':
                points.append((h, w))

    max_step = 0
    for point in points:
        # print(point)
        map = copy.deepcopy(MAP)
        step = search(map, point)
        max_step = max(step, max_step)
    print(max_step)


def search(map, point):
    map[point[0]][point[1]] = "0"

    currents = [point]
    new_points = []
    cost = 1
    while True:
        if len(currents) == 0:
            if len(new_points) == 0:
                # print_map(map)
                return get_max_cost(map)
            currents = new_points
            new_points = []
            cost += 1
        point = currents.pop(0)

        for m in MOVEMENT:
            next_point = (point[0] + m[0], point[1] + m[1])
            if is_valid(map, next_point):
                map[next_point[0]][next_point[1]] = str(cost)
                new_points.append(next_point)


def print_map(map):
    for row in map:
        print("".join(row))


def is_valid(map, point):
    if point[0] < 0 or point[1] < 0:
        return False
    if point[0] >= len(map) or point[1] >= len(map[0]):
        return False
    if map[point[0]][point[1]] == ".":
        return True
    return False


def get_max_cost(map):
    max_cost = 0
    for row in map:
        for col in row:
            if col == '.':
                return None
            elif col == '#':
                continue
            max_cost = max(max_cost, int(col))
    return max_cost


if __name__ == "__main__":
    main()
