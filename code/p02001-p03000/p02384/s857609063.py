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
      
def num_pattern_match(num_list,pattern):
    for i,x in enumerate(num_list):
        is_match=True
        for j,y in enumerate(pattern):
            if num_list[(i+j) % len(num_list)] == pattern[j]:
                pass
            else:
                is_match=False
        if is_match:
            return True
            
    return False      

def build_dice(top,back):
    #2つの面からさいころの状態を初期化する
    dice=Dice()
    dice.top=top
    dice.back=back
    
    dice.bottom=Face(7-int(dice.top))
    dice.front=Face(7-int(dice.back))

    #left-rightはどう計算する?
    #難しく考えないで確実にできる簡単な方法を実行する
    exist_dice_list=[int(dice.top),
    int(dice.bottom),
    int(dice.front),
    int(dice.back)]
    
    left_face_num=set([i+1 for i in range(6)]) - set(exist_dice_list)
    
    #top->front->bottom->backの面のリストを作成する
    #泥臭いプログラミングできるかどうかにかかっている
    face_list=[int(dice.top),int(dice.front),int(dice.bottom),int(dice.back)]

    #泥臭くても手を動かせば完了するときはさっさと手を動かして完了させる
    if 1 in left_face_num:
        #1,5が残されているパターン
        pattern=[2,3,5,4]
        if num_pattern_match(face_list,pattern):
            #top->front->bottom->backに走査したとき、2354に一致するとき
            #左に1が来る
            dice.right=Face.Six
            dice.left=Face.One
        else:
            dice.right=Face.One
            dice.left=Face.Six
            
    elif 2 in left_face_num:
        pattern=[1,4,6,3]
        if num_pattern_match(face_list,pattern):
            dice.right=Face.Five
            dice.left=Face.Two
        else:
            dice.right=Face.Two
            dice.left=Face.Five
            
    elif 3 in left_face_num:
        pattern=[2,6,5,1]
        if num_pattern_match(face_list,pattern):
            dice.right=Face.Four
            dice.left=Face.Three
        else:
            dice.right=Face.Three
            dice.left=Face.Four           
        
    return dice

def run():
    dice_score_ls=list(map(int,input().split()))
    
    dice_score_dict={i+1:score for i,score in enumerate(dice_score_ls)}
    d_inv={v:k for k,v in dice_score_dict.items()}
    
    query_num=int(input())

    for i in range(query_num):
        top,back=tuple(map(int,input().split()))
        top=d_inv[top]
        back=d_inv[back]
        
        dice=build_dice(top,back)
        
        # print(int(dice.right))
        print(dice_score_dict[int(dice.right)])
        


run()
