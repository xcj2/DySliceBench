class Dice(list):
    def __init__(self, *args):
        super().__init__(*args)
        tmp = self[::]
        self._fix_position()
        self.hash = hash(tuple(self))
        self[::] = tmp

    def roll(self, command):
        if command == 'N':
            self[0], self[1], self[5], self[4] = self[1], self[5], self[4], self[0]
        elif command == 'S':
            self[0], self[1], self[5], self[4] = self[4], self[0], self[1], self[5]
        elif command == 'W':
            self[0], self[3], self[5], self[2] = self[2], self[0], self[3], self[5]
        elif command == 'E':
            self[0], self[3], self[5], self[2] = self[3], self[5], self[2], self[0]

    def spin(self, repeat=1):
        for _ in range(repeat):
            self[3], self[1], self[2], self[4] = self[1], self[2], self[4], self[3]

    def _fix_position(self):
        self._min_num_to_top()
        self._min_side_num_to_front()

    def _min_num_to_top(self):
        idx = self.index(min(self))
        if idx == 0:
            pass
        elif idx == 1:
            self.roll('N')
        elif idx == 2:
            self.roll('W')
        elif idx == 3:
            self.roll('E')
        elif idx == 4:
            self.roll('S')
        elif idx == 5:
            self.roll('N')
            self.roll('N')

    def _min_side_num_to_front(self):
        idx = self.index(min(self[3], self[1], self[2], self[4]))
        if idx == 1:
            pass
        elif idx == 2:
            self.spin(1)
        elif idx == 3:
            self.spin(3)
        elif idx == 4:
            self.spin(2)

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return hash(self) == hash(other)


def solve():
    n = int(input())
    dices = set(Dice(map(int, input().split())) for _ in range(n))
    return 'Yes' if n == len(dices) else 'No'


if __name__ == '__main__':
    print(solve())