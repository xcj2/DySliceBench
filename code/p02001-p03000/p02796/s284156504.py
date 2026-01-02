from collections import namedtuple

Robot = namedtuple('Robot', ['end_pos', 'start_pos'])

class Solver:
    def __init__(self, n, robots):
        self.n = n
        self.robots = robots

    def order_by_endpos(self, robots):
        return map(lambda x:Robot(x[0], x[1]), sorted(map(lambda x:(x[0]+x[1], max(x[0]-x[1], 1)), robots)))

    def solve(self):
        current_pos = 0
        keep = 0
        for r in self.order_by_endpos(self.robots):
            if current_pos <= r.start_pos:
                keep += 1
                current_pos = r.end_pos
        return keep


if __name__ == "__main__":
    n = int(input())
    robots = []
    for _ in range(n):
        robots.append(tuple(map(int, input().split())))

    s = Solver(n, robots)
    print(s.solve())
