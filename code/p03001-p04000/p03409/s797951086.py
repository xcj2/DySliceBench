class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __repr__(self):
    #     return '({}, {})'.format(self.x, self.y)

    # def __str__(self):
    #     return '({}, {})'.format(self.x, self.y)


def prepare_points(N, color_str):
    points = []
    for i in range(N):
        tmp = input().split()
        x, y = int(tmp[0]), int(tmp[1])
        point = Point(x, y)
        points.append((point, color_str))
    return points


def main():
    N = int(input())
    red_points = prepare_points(N, 'r')
    blue_points = prepare_points(N, 'b')
    sorted_ = sorted((red_points + blue_points), key=lambda x: x[0].x)
    uses = set()
    count = 0
    for item in sorted_:
        if item[1] == 'r':
            uses.add(item)
        else:
            reds = {
                foo
                for foo in uses if foo[1] == 'r' and foo[0].y < item[0].y
            }
            # print(item, reds)
            if not reds:
                continue
            max_p = max(reds, key=lambda x: x[0].y)
            if max_p[0].y < item[0].y:
                uses.remove(max_p)
                count += 1
    # print(sorted_)
    # print(uses)
    print(count)


if __name__ == '__main__':
    main()