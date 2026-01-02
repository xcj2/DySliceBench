import sys

# 立方体で数字が自由なさいころ
class Dice:
    def __init__(self, top, bottom, front, rear, right, left):
        self.top = top
        self.front = front
        self.right = right
        self.bottom = bottom
        self.rear = rear
        self.left = left

    def rotate_front(self):
        t, b, f, r = self.top, self.bottom, self.front, self.rear
        self.top = r
        self.bottom = f
        self.front = t
        self.rear = b

    def rotate_rear(self):
        t, b, f, r = self.top, self.bottom, self.front, self.rear
        self.top = f
        self.bottom = r
        self.front = b
        self.rear = t

    def rotate_right(self):
        t, b, r, l = self.top, self.bottom, self.right, self.left
        self.top = l
        self.bottom = r
        self.right = t
        self.left = b

    def rotate_left(self):
        t, b, r, l = self.top, self.bottom, self.right, self.left
        self.top = r
        self.bottom = l
        self.right = b
        self.left = t

    def get_tfr(self):
        return [self.top, self.front, self.right]

    def get_all(self):
        return (self.top, self.bottom, self.front, self.rear, self.right, self.left)

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def main():
    n=int(input())
    fin=set()
    top, front, right, left, rear, bottom = map(int, input().split())
    fin.add((top, bottom, front, rear, right, left))
    for _ in range(n-1):
        top, front, right, left, rear, bottom = map(int, input().split())
        d = Dice(top, bottom, front, rear, right, left)
        states = set()
        states.add(d.get_all())
        for _ in range(3):
            d.rotate_right()
            states.add(d.get_all())
        d.rotate_front()
        d.rotate_front()
        states.add(d.get_all())
        for _ in range(3):
            d.rotate_right()
            states.add(d.get_all())

        d.rotate_front()
        states.add(d.get_all())
        for _ in range(3):
            d.rotate_right()
            states.add(d.get_all())
        d.rotate_front()
        d.rotate_front()
        states.add(d.get_all())
        for _ in range(3):
            d.rotate_right()
            states.add(d.get_all())

        d.rotate_right()
        d.rotate_front()
        states.add(d.get_all())
        for _ in range(3):
            d.rotate_right()
            states.add(d.get_all())
        d.rotate_front()
        d.rotate_front()
        states.add(d.get_all())
        for _ in range(3):
            d.rotate_right()
            states.add(d.get_all())

        for t in fin:
            if t in states:
                print("No")
                exit()
    print("Yes")

main()

