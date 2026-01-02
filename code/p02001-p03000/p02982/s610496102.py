import math


def li():
    return list(map(int, input().split()))


def square_distance(point1, point2):
    distance = 0
    for x, y in zip(point1, point2):
        distance = distance + (x - y) ** 2
    return distance


def int_distance(point1, point2):
    return round(math.sqrt(square_distance(point1, point2)))


if __name__ == "__main__":
    [n, d] = li()
    x_list = [li() for _ in range(n)]

    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if square_distance(x_list[i], x_list[j]) == int_distance(x_list[i], x_list[j]) ** 2:
                count = count + 1
    print(count)
