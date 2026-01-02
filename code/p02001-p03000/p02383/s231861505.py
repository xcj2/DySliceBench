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

    inputDiceList = list(map(int, input().split()))
    rollList = list(input())

    d = Dice(inputDiceList)

    for i in rollList:
        d.diceRoll(i)

    print(d.d1)

if __name__ == '__main__':
    main()