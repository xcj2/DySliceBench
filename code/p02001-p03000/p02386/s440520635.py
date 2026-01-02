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
    dice = [Dice(list(map(int, input().split()))) for _ in range(int(input()))]

    for a in range(len(dice)):
        for b in range(a):
            dice_x = dice[a]
            dice_y = dice[b]

            for i in range(4):
                dice_x.rotate("N")
                for j in range(4):
                    dice_x.rotate("E")
                    for k in range(4):
                        dice_x.rotate("R")

                        if dice_x.top != dice_y.top:
                            pass
                        elif dice_x.bottom != dice_y.bottom:
                            pass
                        elif dice_x.left != dice_y.left:
                            pass
                        elif dice_x.right != dice_y.right:
                            pass
                        elif dice_x.front != dice_y.front:
                            pass
                        elif dice_x.back != dice_y.back:
                            pass
                        else:
                            print("No")
                            return
    print("Yes")


if __name__ == "__main__":
    main()

