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


def solve(d1, d2):
    for _ in range(4):
        if d1.top == d2.top and d1.bottom == d2.bottom and d1.front == d2.front and d1.back == d2.back and d1.left == d2.left and d1.right == d2.right:
            return "Yes"
        d2.roll("Z")
    d2.roll("X")
    for _ in range(4):
        if d1.top == d2.top and d1.bottom == d2.bottom and d1.front == d2.front and d1.back == d2.back and d1.left == d2.left and d1.right == d2.right:
            return "Yes"
        d2.roll("Y")
    d2.roll("X")
    for _ in range(4):
        if d1.top == d2.top and d1.bottom == d2.bottom and d1.front == d2.front and d1.back == d2.back and d1.left == d2.left and d1.right == d2.right:
            return "Yes"
        d2.roll("Z")
    d2.roll("X")
    for _ in range(4):
        if d1.top == d2.top and d1.bottom == d2.bottom and d1.front == d2.front and d1.back == d2.back and d1.left == d2.left and d1.right == d2.right:
            return "Yes"
        d2.roll("Y")
    d2.roll("X")
    d2.roll("Y")
    for _ in range(4):
        if d1.top == d2.top and d1.bottom == d2.bottom and d1.front == d2.front and d1.back == d2.back and d1.left == d2.left and d1.right == d2.right:
            return "Yes"
        d2.roll("X")
    d2.roll("Y", 2)
    for _ in range(4):
        if d1.top == d2.top and d1.bottom == d2.bottom and d1.front == d2.front and d1.back == d2.back and d1.left == d2.left and d1.right == d2.right:
            return "Yes"
        d2.roll("X")
    return "No"


labels1 = [int(c) for c in input().split()]
labels2 = [int(c) for c in input().split()]
d1 = Dice(labels1)
d2 = Dice(labels2)
print(solve(d1, d2))

