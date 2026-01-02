import collections


class Dice():

    def __init__(self, labels):
        self.__pip = labels

    def roll_e(self): # 0352 → 3520
        self.__pip[0], self.__pip[3], self.__pip[5], self.__pip[2] = \
            self.__pip[3], self.__pip[5], self.__pip[2], self.__pip[0]

    def roll_n(self): # 0154 → 1540
        self.__pip[0], self.__pip[1], self.__pip[5], self.__pip[4] = \
            self.__pip[1], self.__pip[5], self.__pip[4], self.__pip[0]

    def roll_s(self): # 0451 →  4510
        self.__pip[0], self.__pip[4], self.__pip[5], self.__pip[1] = \
            self.__pip[4], self.__pip[5], self.__pip[1], self.__pip[0]

    def roll_w(self): # 0253 → 2530
        self.__pip[0], self.__pip[2], self.__pip[5], self.__pip[3] = \
            self.__pip[2], self.__pip[5], self.__pip[3], self.__pip[0]

    def roll_nn(self): # 0154 → 5401
        self.roll_n()
        self.roll_n()

    def turn_dice(self): # 1243 → 2431
        self.__pip[1], self.__pip[2], self.__pip[4], self.__pip[3] = \
            self.__pip[2], self.__pip[4], self.__pip[3], self.__pip[1]

    def roll_dice(self, c):
        if c != self.__pip[0]:
            if c == self.__pip[1]:
                self.roll_n()
            elif c == self.__pip[2]:
                self.roll_w()
            elif c == self.__pip[3]:
                self.roll_e()
            elif c == self.__pip[4]:
                self.roll_s()
            else:
                self.roll_nn()

    def get_top(self):
        return self.__pip[0]

    def get_front(self):
        return self.__pip[1]

    def get_right(self):
        return self.__pip[2]
        
    def get_left(self):
        return self.__pip[3]
        
    def get_behind(self):
        return self.__pip[4]
        
    def get_bottom(self):
        return self.__pip[5]

    def judge(self, dice_2):
        top = dice_2.get_top()
        self.roll_dice(top)
        for i in range(4):
            if dice_2.get_front() == self.__pip[1]:
                break
            if i == 3:
                return False
            self.turn_dice()
        if dice_2.get_right() != self.__pip[2] or \
            dice_2.get_left() != self.__pip[3] or \
            dice_2.get_behind() != self.__pip[4] or \
            dice_2.get_bottom() != self.__pip[5]:
            return False
        return True


def main():
    n = int(input())
    *lst, = [input().split() for i in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            lst1 = lst[i]
            lst2 = lst[j]
            if len(set(lst1) ^ set(lst2)) != 0:
                break
            c = collections.Counter(lst2)
            dice1 = Dice(lst1)
            dice2 = Dice(lst2)
            dice2.roll_dice(c.most_common()[-1][0]) # 出現頻度の少ない数字の面を上にする
            if dice1.judge(dice2):
                print('No')
                return
    print('Yes')


if __name__ == "__main__":
    main()

