import sys

A = []

flag_First = True
for Count in range(3):
    for x in input().split(' '):
        x.strip('\n')
        InputValue = int(x)
        if 1<=int(x)<=100:
            if flag_First==True:
                A.append (InputValue)
                flag_First = False
            else:
                for Index in A:
                    if Index == InputValue:
                        print('No')
                        sys.exit()

                A.append (InputValue)
        else:
            print('No')
            sys.exit()

N = int(input())
if N<=0 and N>10:
    print('No')
    sys.exit()

B = []
for Count in range(1,N+1):
    InputValue = int(input())
    if 1<=InputValue<=100:
        if Count == 1:
            B.append (InputValue)
        else:
            for Index in B:
                if Index == InputValue:
                    print('No')
                    sys.exit()

            B.append (InputValue)

Bingo =[0,0,0,0,0,0,0,0,0]

for Item_B in B:
    for Index,Item_A in enumerate(A):
        if Item_A == Item_B:
            Bingo[Index]= 1

def CheckHorizontalBingo(Start,End):

    Flag_Bingo = True
    for Index,Item in enumerate(Bingo):
        if Start<=Index<=End:
            if Item == 0 :
                Flag_Bingo = False

    if Flag_Bingo == True:
        print('Yes')
        sys.exit()

CheckHorizontalBingo(0,2)
CheckHorizontalBingo(3,5)
CheckHorizontalBingo(6,8)

def CheckVerticalBingo(One,Two,There):

    Flag_Bingo = True
    for Index,Item in enumerate(Bingo):
        if Index==One or Index==Two or Index==There:
            if Item == 0 :
                Flag_Bingo = False

    if Flag_Bingo == True:
        print('Yes')
        sys.exit()

CheckVerticalBingo(0,3,6)
CheckVerticalBingo(1,4,7)
CheckVerticalBingo(2,5,8)

def CheckDiagonalBingo(One,Two,There):

    Flag_Bingo = True
    for Index,Item in enumerate(Bingo):
        if Index==One or Index==Two or Index==There:
            if Item == 0 :
                Flag_Bingo = False

    if Flag_Bingo == True:
        print('Yes')
        sys.exit()

CheckDiagonalBingo(0,4,8)
CheckDiagonalBingo(2,4,6)

print('No')