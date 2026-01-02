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


def main():
    diceA_nums = list(map(int, input().split()))
    diceA = Dice(diceA_nums)

    diceB_nums = list(map(int, input().split()))
    diceB = Dice(diceB_nums)

    result = diceB.fit_all(diceA)
    if result == True:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

