from operator import itemgetter
from math import sqrt
from typing import List, Tuple


def distance(p: Tuple[float, float], q: Tuple[float, float]) -> float:
    return sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def closest_distance(points: List[Tuple[float, float]]) -> float:
    def split(i: int, j: int) -> float:
        if j - i < 2:
            return float('INF')
        mid = (i + j) // 2
        d = min(split(i, mid), split(mid, j))
        lv, rv = points[mid][0] - d, points[mid][0] + d
        return merge(sorted([p for p in points[i:j]
                             if lv <= p[0] <= rv], key=itemgetter(1)), d)

    def merge(_points: List[Tuple[float, float]], d: float) -> float:
        n = len(_points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if d < _points[j][1] - _points[i][1]:
                    break
                d = min(d, distance(_points[i], _points[j]))
        return d

    points.sort(key=itemgetter(0, 1))
    return split(0, len(points))


if __name__ == '__main__':
    n = int(input())
    points = [tuple(map(float, input().split())) for _ in range(n)]
    print("{:.6f}".format(closest_distance(points)))  # type: ignore

