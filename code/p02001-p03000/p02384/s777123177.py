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


def main():
    dice_nums = list(map(int, input().split()))
    dice = Dice(dice_nums)

    num_questions = int(input())

    for _ in range(num_questions):
        nums = list(map(int, input().split()))
        dice.fit_top_front(nums[0], nums[1])
        print(dice.right)


if __name__ == "__main__":
    main()

