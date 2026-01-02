
import copy
from enum import IntEnum
import itertools

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
        
    def set_face(self,face_ls):
        self.top=Face(face_ls[0])
        self.back=Face(face_ls[1])
        self.right=Face(face_ls[2])
        self.left=Face(face_ls[3])
        self.front=Face(face_ls[4])
        self.bottom=Face(face_ls[5])
        
    def __str__(self):
        return f"top: {self.top}, back: {self.back}, right: {self.right}, bottom: {self.bottom}, front: {self.front}, left: {self.left}"
        
    def __eq__(self,other):
        equal=self.top == other.top and self.bottom == other.bottom and self.back == other.back and self.front == other.front and self.left == other.left and self.right == other.right
            
        return equal
        
    def get_one_face(self):
        return self.get_n_face(Face.One)
        
    def get_n_face(self,n):
        #指定した面を取得する
        if self.top ==n:
            return self.top
        elif self.bottom==n:
            return self.bottom
        elif self.back==n:
            return self.back
        elif self.front==n:
            return self.front
        elif self.left==n:
            return self.left
        elif self.right==n:
            return self.right
        else:
            assert False
            
    
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
    
    def roll_clockwise_fix_top(self):
        #top,bottomを固定して時計周りに回転させる
        temp=self.front
        self.front=self.left
        self.left=self.back
        self.back=self.right
        self.right=temp
      
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


def move_one_face_to_top(dice):
    #1をトップに持ってくる
    if dice.get_one_face() ==dice.top:
        return
    elif dice.get_one_face()==dice.left:
        #E側に転がす
        dice.roll("E")
        return
    elif dice.get_one_face()==dice.back:
        dice.roll("N")
    elif dice.get_one_face()==dice.right:
        dice.roll("W")
    elif dice.get_one_face()==dice.front:
        dice.roll("S")
    elif dice.get_one_face()==dice.bottom:
        dice.roll("N")
        dice.roll("N")
        

def create_all_equal_dice(dice):
    #等価なダイスをすべて作成する
    same_dice_ls=[]
    for face in list(Face):
        #特定の面を上に回す
        created_dice=copy.deepcopy(dice)
        move_n_face_to_top(created_dice,face)
        same_dice_ls.append(copy.deepcopy(created_dice))
        
        #1,2,3回topを軸にして回転させたものを作成する
        for i in range(3):
            created_dice.roll_clockwise_fix_top()
            same_dice_ls.append(copy.deepcopy(created_dice))
            
    return same_dice_ls
        
def move_n_face_to_top(dice,face):
    #指定した番号をトップに持ってくる
    spec_face=dice.get_n_face(face)
    if spec_face==dice.top:
        return
    elif spec_face==dice.left:
        dice.roll("E")
        return
    elif spec_face==dice.back:
        dice.roll("N")
        return
    elif spec_face==dice.right:
        dice.roll("W")
        return
    elif spec_face==dice.front:
        dice.roll("S")
        return
    elif spec_face==dice.bottom:
        dice.roll("N")
        dice.roll("N")
        return

def move_two_face_to_back(dice):
    #1がtopのときに、2をbackにそろえる
    assert dice.top == Face.One
    assert dice.bottom != Face.Two
    
    if dice.get_n_face(Face.Two)==dice.left:
        dice.roll_clockwise_fix_top()
        dice.roll_clockwise_fix_top()
        dice.roll_clockwise_fix_top()
    elif dice.get_n_face(Face.Two)==dice.front:
        dice.roll_clockwise_fix_top()
        dice.roll_clockwise_fix_top()
    elif dice.get_n_face(Face.Two)==dice.right:
        dice.roll_clockwise_fix_top()


def check_if_equal_dice(dice_x,dice_y):
    #2つの面をそろえて、残りの面を比較すると同じダイスか判定可能
    #1をtopに持ってくるアルゴリズム
    #2をbackに持ってくるアルゴリズム
    #比較する
    
    
    move_one_face_to_top(dice_x)
    move_one_face_to_top(dice_y)
    
    move_two_face_to_back(dice_x)
    move_two_face_to_back(dice_y)
    
    return dice_x==dice_y

def _run():
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
        
    

def _compare_dice_with_dict(dice_x,d_x,dice_y_face_list):
    
    is_top_same=d_x[dice_x.top]==dice_y_face_list[0]
    is_bottom_same=d_x[dice_x.bottom]==dice_y_face_list[5]
    is_right_same=d_x[dice_x.right]==dice_y_face_list[2]
    is_left_same=d_x[dice_x.left]==dice_y_face_list[3]
    is_front_same=d_x[dice_x.front]==dice_y_face_list[4]
    is_back_same=d_x[dice_x.back]==dice_y_face_list[1]
    
    return is_top_same and is_bottom_same and is_right_same and is_left_same and is_front_same and is_back_same

def compare_dice_with_dict(dice_x,d_x,d_y):
    
    is_top_same=d_x[dice_x.top]==d_y[Face.One]
    is_bottom_same=d_x[dice_x.bottom]==d_y[Face.Six]
    is_right_same=d_x[dice_x.right]==d_y[Face.Three]
    is_left_same=d_x[dice_x.left]==d_y[Face.Four]
    is_front_same=d_x[dice_x.front]==d_y[Face.Five]
    is_back_same=d_x[dice_x.back]==d_y[Face.Two]
    
    return is_top_same and is_bottom_same and is_right_same and is_left_same and is_front_same and is_back_same
    
def is_equal_dice(src_face_dict,tgt_face_list,all_dice_ls):

    is_same_dice=False
    for d in all_dice_ls:
        if compare_dice_with_dict(d,src_face_dict,tgt_y_face_list):
            is_same_dice=True
            
    return is_same_dice
    

def run():
    
    dice_num=int(input())
    
    dice_info=[]
    
    dice_face_info=[]
    
    
    for i in range(dice_num):
        ls=list(map(int,input().split()))
        
        dice_info.append(ls)
        
        face_dict={Face(i+1):x for i,x in enumerate(ls)}
        
        dice_face_info.append(face_dict)

    
    #各々のdice_face_dictの組み合わせで比較を行う
    all_dice_ls=create_all_equal_dice(Dice())
    
    is_there_same_dice=False
    for dict_x,dict_y in itertools.combinations(dice_face_info,2):
        for d in all_dice_ls:
            if compare_dice_with_dict(d,dict_x,dict_y):
                is_there_same_dice=True
                
    if is_there_same_dice:
        print("No")
    else:
        print("Yes")
    
    
run()
