from typing import List, Iterator, Tuple


class Rectangle(object):
    def __init__(self, xy1: Tuple[int, int], xy2: Tuple[int, int]) -> None:
        self.topleft = xy1
        self.bottomright = xy2

    def area(self) -> int:
        x1, y1 = self.topleft
        x2, y2 = self.bottomright
        return (x2 - x1) * (y2 - y1)


class MergetdRectangles(object):
    def __init__(self) -> None:
        self.rects: List[Rectangle] = []

    def _intersect(self, base_rect: Rectangle, new_rect: Rectangle) -> bool:
        x1, y1 = base_rect.topleft
        x2, y2 = base_rect.bottomright
        xn1, yn1 = new_rect.topleft
        xn2, yn2 = new_rect.bottomright

        if (xn2 <= x1 or x2 <= xn1):
            return False

        if (yn2 <= y1 or y2 <= yn1):
            return False

        return True

    def _sub(self, base_rect: Rectangle, new_rect: Rectangle) -> Iterator[Rectangle]:
        x1, y1 = base_rect.topleft
        x2, y2 = base_rect.bottomright
        xn1, yn1 = new_rect.topleft
        xn2, yn2 = new_rect.bottomright
        if (x1 < xn1):
            yield Rectangle((x1, y1), (xn1, y2))
        if (xn2 < x2):
            yield Rectangle((xn2, y1), (x2, y2))
        if (y1 < yn1):
            yield Rectangle((max(x1, xn1), y1), (min(x2, xn2), yn1))
        if (yn2 < y2):
            yield Rectangle((max(x1, xn1), yn2), (min(x2, xn2), y2))

    def add(self, new_rect: Rectangle) -> None:
        rects: List[Rectangle] = []
        for r in self.rects:
            if self._intersect(r, new_rect):
                rects.extend(self._sub(r, new_rect))
            else:
                rects.append(r)
        rects.append(new_rect)
        self.rects = rects

    def total_area(self) -> int:
        return sum([r.area() for r in self.rects])


if __name__ == "__main__":
    N = int(input())
    rects = MergetdRectangles()
    for _ in range(N):
        x1, y1, x2, y2 = map(lambda x: int(x), input().split())
        rects.add(Rectangle((x1, y1), (x2, y2)))
    print(rects.total_area())

