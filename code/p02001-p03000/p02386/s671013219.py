def createDice(n):
    dice = []
    for _ in range(n):
        numbers = list(map(int, input().split()))
        dice.append(Dice(numbers))

    return dice

class Dice:
    def __init__(self, numbers):
        self.dice = {"上" :numbers[0],
                     "下":numbers[5], 
                     "前":numbers[1],
                     "後":numbers[4],
                     "左":numbers[3],
                     "右":numbers[2]
                    }

    def query(self):
        return [self.dice["上"], self.dice["下"], self.dice["前"], self.dice["後"], self.dice["左"], self.dice["右"]]

    def rotate_x(self):
        U, D, F, B = [self.dice["上"], self.dice["下"], self.dice["前"], self.dice["後"]]
        self.dice["上"] = F
        self.dice["前"] = D
        self.dice["下"] = B
        self.dice["後"] = U

    def rotate_y(self):
        U, D, L, R = [self.dice["上"], self.dice["下"], self.dice["左"], self.dice["右"]]
        self.dice["上"] = R
        self.dice["下"] = L
        self.dice["左"] = U
        self.dice["右"] = D

    def rotate_z(self):
        F, R, B, L = [self.dice["前"], self.dice["右"], self.dice["後"], self.dice["左"]]
        self.dice["前"] = R
        self.dice["右"] = B
        self.dice["後"] = L
        self.dice["左"] = F

    def set_position(self, position_seq):
        self.ans = []
        self.up = position_seq[0]
        self.front = position_seq[2]
        
        for i in range(6):
            self.search()
            if i == 2:
                self.rotate_y()
            else:
                self.rotate_x()
        
        return self.ans
    
    def search(self):
        # print("goal:上", self.up, ":", self.dice["上"])
        if self.dice["上"] == self.up:
            for _ in range(4):
                # print("goal:前|上 ", self.front, ":", self.dice["前"], "|", self.dice["上"], "→", self.dice["右"])
                if self.dice["前"] == self.front:
                    self.ans.append(self.query())
                    break
                self.rotate_z()

FLAG = 0
n = int(input())
dice = createDice(n)

for i in range(n-1):
    for j in range(i+1, n):
        next_dice = dice[j].query()
        next_dice_seq = dice[j].set_position(next_dice)
        nice_dice_seq = dice[i].set_position(next_dice)
        # print("サイコロ", i, ":", nice_dice_seq)
        # print("サイコロ", j, ":", next_dice_seq)
        # print()

        for k in range(len(nice_dice_seq)):
            for l in range(len(next_dice_seq)):
                FLAG += (nice_dice_seq[k] == next_dice_seq[l])

if FLAG > 0:
    print('No')
else:
    print('Yes')
