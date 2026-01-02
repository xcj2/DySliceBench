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

def is_same():
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
    
top, front, right, left, back, bottom = map(int,input().split())
dice = Dice(top, front, right, left, back, bottom)
top2, front2, right2, left2, back2, bottom2 = map(int,input().split())
dice2 = Dice(top2, front2, right2, left2, back2, bottom2)

if is_same():
    #print(dice.TOP, dice.FRONT, dice.RIGHT, dice.LEFT, dice.BACK, dice.BOTTOM)
    #print(dice2.TOP, dice2.FRONT, dice2.RIGHT, dice2.LEFT, dice2.BACK, dice2.BOTTOM)
    print("Yes")
else:
    #print(dice.TOP, dice.FRONT, dice.RIGHT, dice.LEFT, dice.BACK, dice.BOTTOM)
    #print(dice2.TOP, dice2.FRONT, dice2.RIGHT, dice2.LEFT, dice2.BACK, dice2.BOTTOM)
    print("No")
