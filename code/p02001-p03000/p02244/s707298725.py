import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop

BIG_NUM = 2000000000
HUGE_NUM = 9999999999999999
MOD = 1000000007
EPS = 0.000000001


global H,W
global num_diff
global diff_row,diff_col

def rangeCheck(row,col):
    if row >= 0 and row <= H-1 and col >= 0 and col <= W-1:
        return True
    else:
        return False

#table[row][col]にあるQueenの経路を塗る
def paint(table,row,col):

    table[row][col] = 'Q'

    for i in range(num_diff):

        tmp_row = row+diff_row[i]
        tmp_col = col+diff_col[i]

        while rangeCheck(tmp_row,tmp_col) == True:

            table[tmp_row][tmp_col] = 'x'

            tmp_row += diff_row[i]
            tmp_col += diff_col[i]


#table[row][col]にQueenを置けるか調べる
def is_ok(table,row,col):

    #未定義マスでなければfalse
    if table[row][col] != '.':
        return  False

    #他のQueenと衝突するか調べる
    for i in range(num_diff):

        tmp_row = row+diff_row[i];
        tmp_col = col+diff_col[i];

        while rangeCheck(tmp_row,tmp_col) == True:

            if table[tmp_row][tmp_col] == 'Q':
                return False

            tmp_row += diff_row[i]
            tmp_col += diff_col[i]

    return True


def recursive(base_row,base_col,table,put_num):

    if put_num == 8:

        for row in range(H):
            for col in range(W):

                if table[row][col] == 'Q':

                    print("Q",end = "")
                else:
                    print(".",end = "")
            print()
        return

    #置かないで次へ
    if base_col == 7:
        if base_row == 7:
            return

        recursive(base_row+1,0,table,put_num)

    else:
        recursive(base_row,base_col+1,table,put_num)


    #置けないなら打ち切り
    if is_ok(table,base_row,base_col) == False:
        return

    next_table = [[None]*8 for i in range(8)]

    for row in range(H):
        for col in range(W):
            next_table[row][col] = table[row][col]

    paint(next_table,base_row,base_col)

    if base_col == 7:
        if base_row == 7:
            return
        else:
            recursive(base_row+1,0,next_table,put_num+1)

    else:
        recursive(base_row,base_col+1,next_table,put_num+1)


debug = 0
H = 8
W = 8
num_diff = 8
diff_row = [-1,-1,-1,0,0,1,1,1]
diff_col = [-1,0,1,-1,1,-1,0,1]


N = int(input())
first_table = [['.']*8 for i in range(8)]

for loop in range(N):
    row,col = map(int,input().split())
    paint(first_table,row,col)

recursive(0,0,first_table,N)
