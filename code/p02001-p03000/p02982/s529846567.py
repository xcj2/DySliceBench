import math


def is_distance_integer(p1, p2):
    n = len(p1)

    total = 0
    for i in range(n):
        total += ((p1[i] - p2[i])**2)

    dist = int(math.sqrt(total))

    return (dist**2) == total


def count_pairs(points):
    cnt = 0
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            if is_distance_integer(points[i], points[j]):
                cnt += 1

    return cnt


def main():
    N, D = map(int, input().split())

    points = []
    for _ in range(N):
        points.append(list(map(int, input().split())))

    ans = count_pairs(points)

    print(ans)


main()


