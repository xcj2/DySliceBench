# Dice III
# 2018/11/17, 2019/1/16
from collections import Counter
 
class Dice:
    def __init__(self, *num):
        if len(num) != 6:
            raise ValueError("6!")
        self.numbers = num
 
    def east(self):
        index = (3, 1, 0, 5, 4, 2)
        self.numbers = tuple((self.numbers[i] for i in index))
 
    def west(self):
        index = (2, 1, 5, 0, 4, 3)
        self.numbers = tuple((self.numbers[i] for i in index))
 
    def south(self):
        index = (4, 0, 2, 3, 5, 1)
        self.numbers = tuple((self.numbers[i] for i in index))
 
    def north(self):
        index = (1, 5, 2, 3, 0, 4)
        self.numbers = tuple((self.numbers[i] for i in index))
 
    def rot_top(self):
        """topを変えないように時計周りにくるくる回す"""
        index = (0, 2, 4, 1, 3, 5)
        self.numbers = tuple((self.numbers[i] for i in index))
 
    @property
    def top(self):
        return self.numbers[0]
 
    @property
    def front(self):
        return self.numbers[1]
 
    @property
    def right(self):
        return self.numbers[2]
 
    def __repr__(self):
        return "Dice(" + ", ".join([str(i) for i in self.numbers]) + ")"
 
 
    def align_top_and_front(self, tmp_dice):
        # topを一番レアいやつにする
        rarest = Counter(self.numbers).most_common()[-1][0]
        for i in range(4):
            if self.top == rarest:
                break
            self.east()
        for i in range(4):
            if self.top == rarest:
                break
            self.north()
 
        # topが合うまで回す
        for i in range(4):
            if self.top == tmp_dice.top:
                break
            tmp_dice.east()
 
        for i in range(4):
            if self.top == tmp_dice.top:
                break
            tmp_dice.north()
 
        # frontを合わせる
        for i in range(4):
            if self.front == tmp_dice.front:
                break
            tmp_dice.rot_top()
        return tmp_dice
 
 
    def align(self, other_dice):
        tmp = Dice(*other_dice.numbers)
        tmp = self.align_top_and_front(tmp)
        #print(self.numbers)
        #print(tmp.numbers)
        if self.numbers == tmp.numbers:
            print("Yes")
        else:
            print("No")
 
 
def main():
    num = [int(i) for i in input().split()]
    dice = Dice(*num)
 
    num = [int(i) for i in input().split()]
    other_dice = Dice(*num)
 
    Dice.align(dice, other_dice)
 
if __name__ == "__main__":
    main()
