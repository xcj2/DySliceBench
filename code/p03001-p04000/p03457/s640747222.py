import sys


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def can_move(start, end, time):

    d_x = end.x - start.x
    d_y = end.y - start.y
    if abs(d_x) + abs(d_y) > time:
        return False
    elif abs(d_x) + abs(d_y) == time:
        return True
    else:
        if (abs(d_x) + abs(d_y) - time) % 2 == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    N = int(input())
    prev_point = Point(0, 0)
    prev_time = 0
    for _ in range(N):
        t, x, y = [int(x) for x in input().split(" ")]
        if not can_move(prev_point, Point(x, y), t - prev_time):
            print("No")
            sys.exit(0)
        else:
            prev_time = t
            prev_point = Point(x, y)
    print("Yes")
