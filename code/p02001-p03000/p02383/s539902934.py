class Dice():
    
    def __init__(self, labels):
        self.__pip = labels
        
    def get_top(self):
        return self.__pip[0]
        
    def roll_e(self): # 03520
        self.__pip[0], self.__pip[3], self.__pip[5], self.__pip[2] = \
            self.__pip[3], self.__pip[5], self.__pip[2], self.__pip[0]
            
    def roll_n(self): # 01540
        self.__pip[0], self.__pip[1], self.__pip[5], self.__pip[4] = \
            self.__pip[1], self.__pip[5], self.__pip[4], self.__pip[0]
            
    def roll_s(self): # 04510
        self.__pip[0], self.__pip[4], self.__pip[5], self.__pip[1] = \
            self.__pip[4], self.__pip[5], self.__pip[1], self.__pip[0]
    
    def roll_w(self): # 02530
        self.__pip[0], self.__pip[2], self.__pip[5], self.__pip[3] = \
            self.__pip[2], self.__pip[5], self.__pip[3], self.__pip[0]
    
    def roll_dice(self, command):
        if command == 'E':
            self.roll_e()
        elif command == 'N':
            self.roll_n()
        elif command == 'S':
            self.roll_s()
        else:
            self.roll_w()


def main():
    dice = Dice(list(input().split()))
    commands = input()
    for i in commands:
        dice.roll_dice(i)
    print(dice.get_top())
    
    
if __name__ == "__main__":
    main()

