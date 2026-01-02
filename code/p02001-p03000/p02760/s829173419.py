# -*- coding: utf-8 -*-

#整数値入力 1文字の入力
def input_one_number():
    return int(input())

#整数値龍力　複数の入力
def input_multiple_number():
    return map(int, input().split())

#整数値龍力　複数の入力(配列)
def input_multiple_number_as_list():
    return list(map(int, input().split()))


a= input_multiple_number_as_list()
b= input_multiple_number_as_list()
c = input_multiple_number_as_list()

n= input_one_number()

for i in range(n):
    bq = input_one_number()
    for j in range(3):
        if a[j] == bq:
            a[j] = -1
        if b[j] == bq:
            b[j] = -1
        if c[j] == bq:
            c[j] = -1

if (a[0] == -1 and b[0] == -1 and c[0] == -1) or(a[1] == -1 and b[1] == -1 and c[1] == -1) or (a[2] == -1 and b[2] == -1 and c[2] == -1) or(a[0] == -1 and a[1] == -1 and a[2] == -1) or(b[0] == -1 and b[1] == -1 and b[2] == -1) or(c[0] == -1 and c[1] == -1 and c[2] == -1) or(a[0] == -1 and b[1] == -1 and c[2] == -1) or(a[2] == -1 and b[1] == -1 and c[0] == -1) :
    print("Yes")
else:
    print("No")

