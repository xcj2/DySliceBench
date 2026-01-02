import math


def is_integer(p1, p2):
    total = 0
    for i, j in zip(p1, p2):
        total += (i - j) ** 2
    if math.sqrt(total) * 10 % 10 == 0:
        return True
    else:
        return False


def cnt_integer(points):
    cnt = 0
    size = len(points)

    for i in range(size):
        for j in range(i):
            if is_integer(points[i], points[j]):
                cnt += 1

    return cnt


def main():
    points = []
    N, D = map(int, input().split())

    for _ in range(N):
        points.append(list(map(int, input().split())))

    print(cnt_integer(points))


if __name__ == '__main__':
    main()
