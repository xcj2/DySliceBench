class Dice:
    def __init__(self, top, front, right, left, back, bottom):
        self.TOP = top
        self.BOTTOM = bottom
        self.FRONT = front
        self.BACK = back
        self.LEFT = left
        self.RIGHT = right
    
    def move(self, direction):
        if direction == "N":
            self.move_N()
        elif direction == "E":
            self.move_E()
        elif direction == "S":
            self.move_S()
        elif direction == "W":
            self.move_W()
        elif direction == "SIDE":
            self.move_SIDE()
        else:
            raise Exception
    
    def move_N(self):
        tmp = self.TOP
        self.TOP = self.FRONT
        self.FRONT = self.BOTTOM
        self.BOTTOM = self.BACK
        self.BACK = tmp

    def move_S(self):
        tmp = self.TOP
        self.TOP = self.BACK
        self.BACK = self.BOTTOM
        self.BOTTOM = self.FRONT
        self.FRONT = tmp
        
    def move_W(self):
        tmp = self.TOP
        self.TOP = self.RIGHT
        self.RIGHT = self.BOTTOM
        self.BOTTOM = self.LEFT
        self.LEFT = tmp

    def move_E(self):
        tmp = self.TOP
        self.TOP = self.LEFT
        self.LEFT = self.BOTTOM
        self.BOTTOM = self.RIGHT
        self.RIGHT = tmp
    
    def move_SIDE(self):
        tmp = self.FRONT
        self.FRONT = self.RIGHT
        self.RIGHT = self.BACK
        self.BACK = self.LEFT
        self.LEFT = tmp

def is_same(dice, dice2):
    for _ in range(4):
        dice.move("SIDE")
        for _ in range(4):
            dice.move("N")
            if dice.TOP == dice2.TOP and dice.FRONT == dice2.FRONT \
                and dice.RIGHT == dice2.RIGHT and dice.LEFT == dice2.LEFT \
                and dice.BACK == dice2.BACK and dice.BOTTOM == dice2.BOTTOM:
                return True
        for _ in range(4):
            dice.move("E")
            if dice.TOP == dice2.TOP and dice.FRONT == dice2.FRONT \
                and dice.RIGHT == dice2.RIGHT and dice.LEFT == dice2.LEFT \
                and dice.BACK == dice2.BACK and dice.BOTTOM == dice2.BOTTOM:
                return True
    return False
    
dices = []
n = int(input())
is_OK = True
for _ in range(n):
    top, front, right, left, back, bottom = map(int,input().split())
    new_dice = Dice(top, front, right, left, back, bottom)
    for d in dices:
        if is_same(new_dice, d):
            is_OK = False
            break
    if is_OK == False:
        break
    dices.append(new_dice)
    
if is_OK:
    print("Yes")
else:
    print("No")
