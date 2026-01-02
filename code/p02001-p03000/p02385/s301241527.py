# -*-coding:utf-8

class Dice:

    def __init__(self, diceList):
        self.d1, self.d2, self.d3, self.d4, self.d5, self.d6 = diceList

    def diceRoll(self, r):
        if(r == 'N'):
            self.d1, self.d2, self.d5, self.d6 = self.d2, self.d6, self.d1, self.d5

        elif(r == 'E'):
            self.d1, self.d3, self.d4, self.d6 = self.d4, self.d1, self.d6, self.d3

        elif(r == 'W'):
            self.d1, self.d3, self.d4, self.d6 = self.d3, self.d6, self.d1, self.d4

        elif(r == 'S'):
            self.d1, self.d2, self.d5, self.d6 = self.d5, self.d1, self.d6, self.d2


def main():

    orderList = ['N', 'E', 'W', 'S']
    inputDiceList1 = list(map(int, input().split()))
    inputDiceList2 = list(map(int, input().split()))

    dice1 = Dice(inputDiceList1)
    dice2 = Dice(inputDiceList2)

    cmd = "N" * 4 + ("W" + "N" * 4) * 3 + "NE" + "N" * 4 + "EE" + "N" * 4

    for i in cmd:
        if(dice1.d1 == dice2.d1 and dice1.d2 == dice2.d2 and dice1.d3 == dice2.d3 and dice1.d4 == dice2.d4 and dice1.d5 == dice2.d5 and dice1.d6 == dice2.d6):
            print('Yes')
            return 0
        else:
            dice2.diceRoll(i)

    print('No')

if __name__ == '__main__':
    main()