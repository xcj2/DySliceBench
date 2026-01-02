class Bar:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.left = False
        self.center = False
        self.right = False

    def open(self, v):
        if v == self.a:
            self.left = True
        elif v == self.b:
            self.center = True
        elif v == self.c:
            self.right = True

    def bingo(self):
        return all([self.left, self.right, self.center])


top = Bar(*map(int, input().split()))
center = Bar(*map(int, input().split()))
bottom = Bar(*map(int, input().split()))
for x in range(int(input())):
    value = int(input())
    top.open(value)
    center.open(value)
    bottom.open(value)


def ok():
    print("Yes")
    exit()


if top.bingo() or center.bingo() or bottom.bingo():
    ok()

if top.left == center.left == bottom.left == True:
    ok()

if top.center == center.center == bottom.center == True:
    ok()

if top.right == center.right == bottom.right == True:
    ok()

if top.left == center.center == bottom.right == True:
    ok()

if top.right == center.center == bottom.left == True:
    ok()

print('No')


