# https://beta.atcoder.jp/contests/abc057/tasks/abc057_b
class Point(object):
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    @staticmethod
    def manhattan(p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def solve():
    # Max(n, m) = (50, 50) => 50 * 2
    n, m = map(int, input().split())
    students = []
    for _ in range(n):
        students.append(Point(*input().split()))

    checkpoints = []
    for _ in range(m):
        checkpoints.append(Point(*input().split()))

    for student in students:
        min_dist = 4 * (10 ** 8)
        min_index = 1
        for index, cp in enumerate(checkpoints):
            manhattan = Point.manhattan(student, cp)
            if min_dist > manhattan:
                min_dist = manhattan
                min_index = index + 1
        print(min_index)


if __name__ == '__main__':
    solve()
