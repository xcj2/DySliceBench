class Dice:

    __top = 0
    __front = 1
    __right = 2
    __left = 3
    __back = 4
    __bottom = 5

    def __init__(self, a, b, c, d, e, f):
        self.__dice = [a,b,c,d,e,f]

    def S(self):
        dice_before = self.__dice[:]
        self.__dice[Dice.__top]    = dice_before[Dice.__back]
        self.__dice[Dice.__front]  = dice_before[Dice.__top]
        self.__dice[Dice.__right]  = dice_before[Dice.__right]
        self.__dice[Dice.__left]   = dice_before[Dice.__left]
        self.__dice[Dice.__back]   = dice_before[Dice.__bottom]
        self.__dice[Dice.__bottom] = dice_before[Dice.__front]

    def E(self):
        dice_before = self.__dice[:]
        self.__dice[Dice.__top]    = dice_before[Dice.__left]
        self.__dice[Dice.__front]  = dice_before[Dice.__front]
        self.__dice[Dice.__right]  = dice_before[Dice.__top]
        self.__dice[Dice.__left]   = dice_before[Dice.__bottom]
        self.__dice[Dice.__back]   = dice_before[Dice.__back]
        self.__dice[Dice.__bottom] = dice_before[Dice.__right]

    def W(self):
        dice_before = self.__dice[:]
        self.__dice[Dice.__top]    = dice_before[Dice.__right]
        self.__dice[Dice.__front]  = dice_before[Dice.__front]
        self.__dice[Dice.__right]  = dice_before[Dice.__bottom]
        self.__dice[Dice.__left]   = dice_before[Dice.__top]
        self.__dice[Dice.__back]   = dice_before[Dice.__back]
        self.__dice[Dice.__bottom] = dice_before[Dice.__left]

    def N(self):
        dice_before = self.__dice[:]
        self.__dice[Dice.__top]    = dice_before[Dice.__front]
        self.__dice[Dice.__front]  = dice_before[Dice.__bottom]
        self.__dice[Dice.__right]  = dice_before[Dice.__right]
        self.__dice[Dice.__left]   = dice_before[Dice.__left]
        self.__dice[Dice.__back]   = dice_before[Dice.__top]
        self.__dice[Dice.__bottom] = dice_before[Dice.__back]

    def turn(self):
        dice_before = self.__dice[:]
        self.__dice[Dice.__top]    = dice_before[Dice.__top]
        self.__dice[Dice.__front]  = dice_before[Dice.__right]
        self.__dice[Dice.__right]  = dice_before[Dice.__back]
        self.__dice[Dice.__left]   = dice_before[Dice.__front]
        self.__dice[Dice.__back]   = dice_before[Dice.__left]
        self.__dice[Dice.__bottom] = dice_before[Dice.__bottom]

    def top(self):
        return(self.__dice[Dice.__top])

    def front(self):
        return(self.__dice[Dice.__front])

    def right(self):
        return(self.__dice[Dice.__right])

    def left(self):
        return(self.__dice[Dice.__left])

    def back(self):
        return(self.__dice[Dice.__back])

    def bottom(self):
        return(self.__dice[Dice.__bottom])

    def compare(self, dice):
        if (self.__dice[Dice.__top]    == dice.__dice[Dice.__top] and
            self.__dice[Dice.__front]  == dice.__dice[Dice.__front] and
            self.__dice[Dice.__right]  == dice.__dice[Dice.__right] and
            self.__dice[Dice.__left]   == dice.__dice[Dice.__left] and
            self.__dice[Dice.__back]   == dice.__dice[Dice.__back] and
            self.__dice[Dice.__bottom] == dice.__dice[Dice.__bottom]):
            print("Yes")
        else:
            print("No")

    def print(self):
        print('[top   ] :', self.__dice[Dice.__top])
        print('[front ] :', self.__dice[Dice.__front])
        print('[right ] :', self.__dice[Dice.__right])
        print('[left  ] :', self.__dice[Dice.__left])
        print('[back  ] :', self.__dice[Dice.__back])
        print('[bottom] :', self.__dice[Dice.__bottom])


def S(dice, top):
    for t in range(4):
        if dice.top() == top:
            return dice
        dice.S()
    return dice

def turn(dice, front):
    for t in range(4):
        if dice.front() == front:
            return dice
        dice.turn()
    return dice

a, b, c, d, e, f = input().split()
dice1 = Dice(a, b, c, d, e, f)

top = max(a,b,c,d,e,f)
dice1 = S(dice1, top)
a,b,c,d,e,f = input().split()
dice2 = Dice(a,b,c,d,e,f)

top = dice1.top()
front = dice1.front()

for to in range(2):
    dice2 = S(dice2, top)
    if dice2.top() == top:
        break
    else:
        dice2.turn()

for fr in range(4):
    dice2 = turn(dice2, front)
    if dice2.front() == front:
        break

dice1.compare(dice2)