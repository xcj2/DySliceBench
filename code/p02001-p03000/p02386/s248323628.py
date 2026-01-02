class Dice():
    def __init__(self):
        self.num = [0 for _ in range(6)]
    
    def set_num(self, n0, n1, n2, n3, n4, n5):
        self.num[0] = n0
        self.num[1] = n1
        self.num[2] = n2
        self.num[3] = n3
        self.num[4] = n4
        self.num[5] = n5
    
    
    def roll(self, order):
        tmp = self.num.copy()
        
        if order == "N":
            self.set_num(tmp[1], tmp[5], tmp[2], tmp[3], tmp[0], tmp[4])
        elif order == "S":
            self.set_num(tmp[4], tmp[0], tmp[2], tmp[3], tmp[5], tmp[1])
        elif order == "E":
            self.set_num(tmp[3], tmp[1], tmp[0], tmp[5], tmp[4], tmp[2])
        elif order == "W":
            self.set_num(tmp[2], tmp[1], tmp[5], tmp[0], tmp[4], tmp[3])
        elif order == "rot_Clock":
            self.set_num(tmp[0], tmp[2], tmp[4], tmp[1], tmp[3], tmp[5])
        else:
            print("Error: 不正な入力です")

    def get_top_num(self):
        return self.num[0]
        

    
# Input
n_dice = int(input())
list_dice_num = []
for _ in range(n_dice):
    list_dice_num.append([int(_) for _ in input().split()])

# Set Dice
list_dice = []
for init_num1 in list_dice_num:
    dice1 = Dice()
    dice1.set_num(init_num1[0], init_num1[1], init_num1[2], init_num1[3], init_num1[4], init_num1[5])
    list_dice.append(dice1)

# 1st way
def check_dice_equal_1(dice1, dice2):
    checker = False
    for i in range(3):
        for j in range(3):
            orders = "N" * (i + 1) + "E" * (j + 1)
            # print(orders)
            
            for order in orders:
                dice2.roll(order)
            if dice1.num == dice2.num:
                checker = True
            
    for i in range(3):
        for j in range(3):
            orders = "E" * (i + 1) + "N" * (j + 1)
            # print(orders)
            
            for order in orders:
                dice2.roll(order)
            if dice1.num == dice2.num:
                checker = True
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                orders = "E" * (i + 1) + "N" * (j + 1) + "E" * (k + 1)
                # print(orders)
                
                for order in orders:
                    dice2.roll(order)
                if dice1.num == dice2.num:
                    checker = True
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                orders = "N" * (i + 1) + "E" * (j + 1) + "N" * (k + 1)
                # print(orders)
                
                for order in orders:
                    dice2.roll(order)
                if dice1.num == dice2.num:
                    checker = True
    return checker

# 2nd way
def check_dice_equal_2(dice1, dice2):
    checker = False
    num_dice1_top, num_dice1_front = dice1.num[0], dice1.num[1]
    
    index_top = dice2.num.index(num_dice1_top)
    index_front = dice2.num.index(num_dice1_front)
    
    counter = 0
    while (index_top != 0) & (counter < 3):
        counter += 1
        if index_top in [0, 1, 4, 5]:
            dice2.roll("N")
            index_top = dice2.num.index(num_dice1_top)
            index_front = dice2.num.index(num_dice1_front)
        else:
            dice2.roll("E")
            index_top = dice2.num.index(num_dice1_top)
            index_front = dice2.num.index(num_dice1_front)
    
    counter = 0
    while (index_front != 1) & (counter < 3):
            dice2.roll("rot_Clock")
            index_top = dice2.num.index(num_dice1_top)
            index_front = dice2.num.index(num_dice1_front)
    
    # print(f"dice1: {dice1.num}")
    # print(f"dice2: {dice2.num}")
    
    if dice1.num == dice2.num:
        checker = True
        
    return checker


# Main
ans_checker = True
for i in range(len(list_dice) - 1):
    for j in range(len(list_dice) - i - 1):
        j2 = j + (i + 1)
        dice1 = list_dice[i]
        dice2 = list_dice[j2]
        
        checker1 = check_dice_equal_1(dice1, dice2)
        checker2 = check_dice_equal_1(dice1, dice2)
        
        # どちらかがTrue(同じサイコロならFalse)
        if checker1 or checker2:
            ans_checker = False
    
if ans_checker:
    print("Yes")
else:
    print("No")

