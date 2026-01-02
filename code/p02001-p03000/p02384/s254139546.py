class Dice():
    def __init__(self, labels):
        self.top = labels[0]
        self.front = labels[1]
        self.right = labels[2]
        self.left = labels[3]
        self.back = labels[4]
        self.bottom = labels[5]

    def roll(self, axis, count=1):
        while count < 0:
            count += 4
        if axis == "X":
            for _ in range(count):
                self.top, self.back, self.bottom, self.front = self.front, self.top, self.back, self.bottom
        elif axis == "Y":
            for _ in range(count):
                self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom
        elif axis == "Z":
            for _ in range(count):
                self.front, self.left, self.back, self.right = self.right, self.front, self.left, self.back
        elif axis == "N":
            self.roll("X", 1)
        elif axis == "W":
            self.roll("Y", -1)
        elif axis == "S":
            self.roll("X", -1)
        elif axis == "E":
            self.roll("Y", 1)


def solve(d, top, front):
    for _ in range(4):
        if d.top == top and d.front == front:
            return d.right
        d.roll("Z")
    d.roll("X")
    for _ in range(4):
        if d.top == top and d.front == front:
            return d.right
        d.roll("Y")
    d.roll("X")
    for _ in range(4):
        if d.top == top and d.front == front:
            return d.right
        d.roll("Z")
    d.roll("X")
    for _ in range(4):
        if d.top == top and d.front == front:
            return d.right
        d.roll("Y")
    d.roll("X")
    d.roll("Y")
    for _ in range(4):
        if d.top == top and d.front == front:
            return d.right
        d.roll("X")
    d.roll("Y", 2)
    for _ in range(4):
        if d.top == top and d.front == front:
            return d.right
        d.roll("X")


labels = [int(c) for c in input().split()]
d = Dice(labels)
q = int(input())
for _ in range(q):
    top, front = map(int, input().split())
    print(solve(d, top, front))

