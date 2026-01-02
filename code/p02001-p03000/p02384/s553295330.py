class Dice(object):
    def __init__(self, faces):
        self.top = faces[0]
        self.front = faces[1]
        self.right = faces[2]
        self.left = faces[3]
        self.back = faces[4]
        self.bottom = faces[5]

    def rotate(self, command):
        pre_top = self.top
        if command == "N":
            self.top = self.front
            self.front = self.bottom
            self.bottom = self.back
            self.back = pre_top
        elif command == "E":
            self.top = self.left
            self.left = self.bottom
            self.bottom = self.right
            self.right = pre_top
        elif command == "W":
            self.top = self.right
            self.right = self.bottom
            self.bottom = self.left
            self.left = pre_top
        elif command == "S":
            self.top = self.back
            self.back = self.bottom
            self.bottom = self.front
            self.front = pre_top
        elif command == "R":
            pre_front = self.front
            self.front = self.left
            self.left = self.back
            self.back = self.right
            self.right = pre_front


def main() -> None:
    dice_values = list(map(int, input().split()))
    dice_x = Dice(dice_values)

    q = int(input())
    for i in range(q):
        top, front = map(int, input().split())
        for j in range(6):
            if top == dice_x.top:
                break
            dice_x.rotate("N")
        for j in range(6):
            if top == dice_x.top:
                break
            dice_x.rotate("E")
        while front != dice_x.front:
            dice_x.rotate("R")
        print(dice_x.right)


if __name__ == "__main__":
    main()
