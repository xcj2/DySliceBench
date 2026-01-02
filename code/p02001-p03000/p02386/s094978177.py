import itertools
class Dice:
    def __init__(self, labels):
        self.labels = labels
        self.up = labels[0]
        self.front = labels[1]
        self.right = labels[2]
        self.left = labels[3]
        self.back = labels[4]
        self.down = labels[5]
    def east(self):
        self.up, self.right, self.down, self.left = self.left, self.up, self.right, self.down
        self.update_labels()
    def north(self):
        self.up, self.back, self.down, self.front = self.front, self.up, self.back, self.down
        self.update_labels()
    def south(self):
        self.up, self.front, self.down, self.back = self.back, self.up, self.front, self.down
        self.update_labels()
    def west(self):
        self.up, self.left, self.down, self.right = self.right, self.up, self.left, self.down
        self.update_labels()
    def clockwise(self):
        self.front, self.left, self.back, self.right = self.right, self.front, self.left, self.back
        self.update_labels()
    def counterclockwise(self):
        self.front, self.right, self.back, self.left = self.left, self.front, self.right, self.back
        self.update_labels()
    def set_up(self, up):
        for i in range(6):
            if up == self.up:
                break
            if i % 2:
                self.east()
            else:
                self.north()
    def set_front(self, front):
        while True:
            if front == self.front:
                break
            self.clockwise()
    def update_labels(self):
        self.labels = [self.up, self.front, self.right, self.left, self.back, self.down]

def is_the_same(d1, d2):
    for i in range(30):
        if d1.labels == d2.labels:
            return True
        if i % 5 == 0:
            if i % 10 == 0:
                d2.east()
            else:
                d2.north()
        else:
            d2.clockwise()
    else:
        return False

n = int(input())
dices = []
for _ in range(n):
    dices.append(Dice(list(map(int, input().split()))))
for d in itertools.combinations(dices, 2):
    if is_the_same(d[0], d[1]):
        print('No')
        break
else:
    print('Yes')