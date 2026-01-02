class Dice:
    def __init__(self, nums):
        self.top    = nums[0]
        self.front  = nums[1]
        self.right  = nums[2]
        self.left   = nums[3]
        self.back   = nums[4]
        self.bottom = nums[5]

    def toN(self):
        tmp = self.top
        self.top = self.front
        self.front = self.bottom
        self.bottom = self.back
        self.back = tmp

    def toS(self):
        tmp = self.top
        self.top = self.back
        self.back = self.bottom
        self.bottom = self.front
        self.front = tmp

    def toE(self):
        tmp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = tmp

    def toW(self):
        tmp = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = tmp

    def moveTo(self, ds):
        for d in ds:
            if   d == 'N':
                self.toN()
            if d == 'S':
                self.toS()
            if d == 'E':
                self.toE()
            if d == 'W':
                self.toW()

    def getTop(self):
        return self.top

    def getBottom(self):
        return self.bottom

    def getFront(self):
        return self.front

    def getBack(self):
        return self.back

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def __eq__(self, other):
        if self.top != other.top:
            return False
        if self.bottom != other.bottom:
            return False
        if self.front != other.front:
            return False
        if self.back != other.back:
            return False
        if self.left != other.left:
            return False
        if self.right != other.right:
            return False

        return True

def moveTo(dice, top, front):
    if dice.getFront() != front:
        if   dice.getTop()    == front:
            dice.moveTo("S")
        elif dice.getBottom() == front:
            dice.moveTo("N")
        elif dice.getBack()   == front:
            dice.moveTo("NN")
        elif dice.getLeft()   == front:
            dice.moveTo("ES")
        elif dice.getRight()  == front:
            dice.moveTo("WS")

    if dice.getTop() != top:
        if   dice.getBottom() == top:
            dice.moveTo("EE")
        elif dice.getLeft()   == top:
            dice.moveTo("E")
        elif dice.getRight()  == top:
            dice.moveTo("W")

    return dice

def equalDice(dice1, dice2):
    dice2 = moveTo(dice2, dice1.getTop(), dice1.getFront())
    return dice1 == dice2

def main():
    dice1 = Dice(input().split())
    dice2 = Dice(input().split())

    if equalDice(dice1, dice2):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

