#■標準入力ショートカット


def get_next_int():
    return int(float(input()))


def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])


def get_next_str():
    return input()


def get_next_strs(delim=" "):
    return tuple(input().split(delim))


def get_next_by_types(*value_types, delim=" "):
    return tuple([t(x) for t, x in zip(value_types, input().split(delim))])


class Grid():

    def __init__(self):
        self.H, self.W = get_next_ints()
        self.canvas = []
        for i in range(self.H):
            self.canvas.append(get_next_str())

    def check(self, x, y):
        checker = False
        if x-1 >= 0:
            checker = checker or self.canvas[y][x-1] == '#'
        if x+1 < self.W:
            checker = checker or self.canvas[y][x+1] == '#'
        if y-1 >= 0:
            checker = checker or self.canvas[y-1][x] == '#'
        if y+1 < self.H:
            checker = checker or self.canvas[y+1][x] == '#'
        return checker

    def solve(self):
        available = True
        for y in range(self.H):
            if not available:
                break
            for x in range(self.W):
                if self.canvas[y][x] == '#':
                    available = available and self.check(x, y)
        if available:
            print('Yes')
        else:
            print('No')


def solve():
    g = Grid()
    g.solve()
    
solve()