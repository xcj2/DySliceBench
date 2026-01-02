class Dice():
    directions = "EEENEEENEEESEEESEEENEEEN"

    def __init__(self, lst):
        self.top = lst[0]
        self.front = lst[1]
        self.right = lst[2]
        self.left = lst[3]
        self.back = lst[4]
        self.bottom = lst[5]

    def rotate(self, direction):
        if direction == "E":
            self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom
        if direction == "N":
            self.top, self.back, self.bottom, self.front = self.front, self.top, self.back, self.bottom
        if direction == "S":
            self.top, self.front, self.bottom, self.back = self.back, self.top, self.front, self.bottom
        if direction == "W":
            self.top, self.left, self.bottom, self.right = self.right, self.top, self.left, self.bottom

    def fit_top_front(self, num_top, num_front):
        for direction in Dice.directions:
            if self.top == num_top and self.front == num_front:
                break
            self.rotate(direction)

    def fit_all(self, dice):
        for direction in Dice.directions:
            if self.top == dice.top and self.front == dice.front and self.right == dice.right and self.left == dice.left and self.back == dice.back and self.bottom == dice.bottom:
                return True
            self.rotate(direction)
        return False


def compare(lst, dice):
    for direction in Dice.directions:
        if lst[0] == dice.top and lst[1] == dice.front and lst[2] == dice.right and lst[3] == dice.left and lst[4] == dice.back and lst[5] == dice.bottom:
            return True
        dice.rotate(direction)
    return False


def main():
    num_dices = int(input())  # number of dices
    dices = []  # label of dices
    dices.append(list(map(int, input().split())))  # first dice
    for _ in range(num_dices - 1):
        label_dice = list(map(int, input().split()))
        dice = Dice(label_dice)
        for i in range(len(dices)):
            result = compare(dices[i], dice)
            if result == True:
                print("No")
                return 0
        dices.append(label_dice)
    print("Yes")


if __name__ == "__main__":
    main()

