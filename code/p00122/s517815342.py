class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return self.x * 10 + self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def create_water_range():
    l = []

    for item in [-1, 0, 1]:
        for item2 in [-1, 0, 1]:
            l.append(Vector2(item, item2))

    return l


def create_jump_range():
    l = []

    for item in [-2, 2]:
        for item2 in [-1, 0, 1]:
            l.append(Vector2(item, item2))
            l.append(Vector2(item2, item))

    return l


WATER_RANGE = create_water_range()
JUMP_RANGE = create_jump_range()


def is_live(water_count, point, LIMIT, WATER_POINT_LIST):
    if LIMIT <= water_count:
        return True

    center = WATER_POINT_LIST[water_count]

    water_point_set = set(center + water for water in WATER_RANGE)

    for jump in JUMP_RANGE:
        new_point = point + jump

        if 0 <= new_point.x <= 9 and 0 <= new_point.y <= 9:
            if new_point in water_point_set:
                result = is_live(water_count + 1, new_point, LIMIT, WATER_POINT_LIST)

                if result:
                    return result

    return False


while True:
    x, y = [int(item) for item in input().split(" ")]

    if x == 0 and y == 0:
        break

    my_point = Vector2(x, y)

    water_count = int(input())
    point_list = [int(item) for item in input().split(" ")]

    water_point_list = []

    for x, y in zip(point_list[::2], point_list[1::2]):
        water_point_list.append(Vector2(x, y))

    result = is_live(0, my_point, water_count, water_point_list)

    if result:
        print("OK")
    else:
        print("NA")

