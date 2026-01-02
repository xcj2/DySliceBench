from enum import IntEnum

class Face(IntEnum):
    One=1
    Two=2
    Three=3
    Four=4
    Five=5
    Six=6


class Dice:
    def __init__(self):
        self.top=Face.One
        self.bottom=Face.Six
        self.back=Face.Two
        self.front=Face.Five
        self.left=Face.Four
        self.right=Face.Three
    
    def roll(self,command):
        if command=="E":
            #back-frontを軸として右回転
            temp=self.top
            self.top=self.left
            self.left=self.bottom
            self.bottom=self.right
            self.right=temp
            
        elif command=="N":
            #right-leftを固定して前転
            temp=self.top
            self.top=self.back
            self.back=self.bottom
            self.bottom=self.front
            self.front=temp
            
        elif command=="S":
            #right-leftを固定して後転
            temp=self.top
            self.top=self.front
            self.front=self.bottom
            self.bottom=self.back
            self.back=temp
            
        elif command=="W":
            #back-frontを軸として左回転
            temp=self.top
            self.top=self.right
            self.right=self.bottom
            self.bottom=self.left
            self.left=temp
            



def run():
    dice_score_ls=list(map(int,input().split()))
    command_str=input()
    
    dice_score_dict={i+1:score for i,score in enumerate(dice_score_ls)}
    
    dice=Dice()
    for command in command_str:
        dice.roll(command)
        

    final_score=dice_score_dict[int(dice.top)]
    print(f"{final_score}")


run()
