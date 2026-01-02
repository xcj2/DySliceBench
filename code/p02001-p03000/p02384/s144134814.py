# -*-coding:utf-8

import random

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
    inputDiceList = list(map(int, input().split()))
    inputNum = int(input())
    d = Dice(inputDiceList)

    for i in range(inputNum):
        x, y = map(int, input().split())
        while True:
            if(d.d1 == x and d.d2 == y):
                print(d.d3)
                break
            else:
                r = random.randint(0, 3)
                d.diceRoll(orderList[r])

if __name__ == '__main__':
    main()