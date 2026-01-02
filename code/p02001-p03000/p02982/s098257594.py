import itertools


def calc_dist(p1, p2):
    return sum([(i - j) ** 2 for i, j in zip(p1, p2)])


def is_integer(p1, p2):
    dist = calc_dist(p1, p2)
    if pow(dist, 0.5).is_integer():
        return True
    else:
        return False


def main():
    points = []
    N, D = map(int, input().split())

    for _ in range(N):
        points.append(list(map(int, input().split())))

    cnt = 0
    for pair in list(itertools.combinations(points, 2)):
        if is_integer(pair[0], pair[1]):
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
