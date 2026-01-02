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
            
    def get_right(self, top, front):
        if top != self.__pip[0]:
            if top == self.__pip[1]:
                self.roll_n()
            elif top == self.__pip[2]:
                self.roll_w()
            elif top == self.__pip[3]:
                self.roll_e()
            elif top == self.__pip[4]:
                self.roll_s()
            else:
                self.roll_nn()
        for i in range(3):
            if front == self.__pip[1]:
                break
            self.turn_dice()
        return self.__pip[2]
        
        
def main():
    dice = Dice(list(input().split()))
    n = int(input())
    for i in range(n):
        top, front = input().split()
        right = dice.get_right(top, front)
        print("{}".format(right))
        

if __name__ == "__main__":
    main()

