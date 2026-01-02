
import math


def read_input():
    n, d = map(int, input().split())

    points = []
    for i in range(n):
        point = list(map(int, input().split()))
        points.append(point)

    return n, d, points


def check_good_distance(p1, p2):
    dist = 0
    for e1, e2 in zip(p1, p2):
        temp = abs(e2 - e1)
        dist += temp ** 2

    dist = math.sqrt(dist)

    if dist == int(dist):
        return True
    else:
        return False


def submit():
    n, d, points = read_input()

    count = 0
    for i, p1 in enumerate(points):
        for p2 in points[i+1:]:
            if check_good_distance(p1, p2):
                count += 1

    print(count)




if __name__ == '__main__':
    submit()
