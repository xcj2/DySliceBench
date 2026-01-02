class Coordinate(object):
    def __init__(self):
        self.path = [None, None, None, None]


class Maze(object):
    def __init__(self):
        self.a = [[Coordinate() for _ in [0]*5] for _ in [0]*5]

    def get_room(self, x, y):
        return self.a[y][x]

    def set_path(self, pos1, pos2):
        dir1, dir2 = (0, 2) if pos1[1] == pos2[1] else (1, 3)
        self.get_room(*pos1).path[dir1] = pos2
        self.get_room(*pos2).path[dir2] = pos1

    def solve(self):
        result, x, y, direction = "R", 1, 0, 0
        direction_sign = "RDLU"

        while not(x == 0 and y == 0):
            current = self.get_room(x, y)
            if current.path[(direction-1)%4]:
                direction = (direction-1)%4
            elif current.path[direction]:
                pass
            elif current.path[(direction+1)%4]:
                direction = (direction+1)%4
            else:
                direction = (direction+2)%4
            x, y = current.path[direction]
            result += direction_sign[direction]

        return result


maze = Maze()
for i in range(9):
    y = i//2
    dx, dy = (1, 0) if i%2 == 0 else (0, 1)
    for x, c in enumerate(input()):
        if c == "1":
            maze.set_path((x, y), (x+dx, y+dy))

print(maze.solve())
