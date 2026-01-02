#! /usr/bin/python
# -*- coding: utf-8 -*-
# ALDS1_2_C: Stable Sort

import copy

def BubbleSort(A, N):
    minj = 0
    tmp = 0
    flag = 1

    for i in range(1, N):
        for j in reversed(range(i, N)):
            if A[j][1] < A[j-1][1]:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
    # while flag:
    #     flag = 0    #数値の転倒があることを表すflagを定義
    #     for i in range(1, N):
    #         j = N - i   #末尾から見ていくための変数jを定義
    #         if A[j][1] < A[j-1][1]:   #転倒があるとき
    #             tmp = A[j]  #この行から下の2行目までで、転倒のある部分を入れ替える
    #             A[j] = A[j-1]
    #             A[j-1] = tmp
    #             flag = 1    #転倒があったことを表すflagを立てる。1度入れ替えたところで他にも入れ替えの必要がある要素がある可能性はあるので、そのためのフラグ。
    return A

def SelectionSort(A, N):
    minj = 0
    tmp = 0
    flag = 1
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j][1] < A[minj][1]:  #一番小さい要素よりも小さいものを記憶する
                minj = j
        tmp = A[i]  #一番小さい要素とi番目の要素を入れ替え
        A[i] = A[minj]
        A[minj] = tmp
        
    return A

def isStable(list1, list2, N):
    for i in range(0, N):
        if list1[i][0] != list2[i][0]:
            print("Not stable")
            return 0
    print("Stable")
    return 0

if __name__ == "__main__":
    N=int(input()) # 数列の長さ
    A=list(input().split()) # 空白を区切文字として配列に格納
    L1 = copy.deepcopy(A)
    L2 = copy.deepcopy(A)
    # print(id(L1), id(L2))
    A1 = BubbleSort(L1, N)
    A2 = SelectionSort(L2, N)
    print(*A1)
    print("Stable")
    print(*A2)
    isStable(A1, A2, N)
    
    
