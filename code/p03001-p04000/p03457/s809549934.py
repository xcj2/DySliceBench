
def read_input():
    n = int(input())

    points = [[0, 0, 0]]
    for i in range(n):
        points.append(list(map(int, input().split())))

    return n, points


def check_transition(point1, point2):
    t_diff = point2[0] - point1[0]
    x_diff = point2[1] - point1[1]
    y_diff = point2[2] - point1[2]

    x_diff = abs(x_diff)
    y_diff = abs(y_diff)

    distance = x_diff + y_diff

    if t_diff >= distance:
        if t_diff % 2 == distance % 2:
            return True

    return False


def check_all_transition():
    n, points = read_input()
    for p1, p2 in zip(points, points[1:]):
        if not check_transition(p1, p2):
            return False
    return True


if check_all_transition():
    print('Yes')
else:
    print('No')