# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 09:21:55 2018
ALDS-1-2c
@author: maezawa
"""

def selection(a, n):
    """
    Selection Sort of array a, n=len(a)
    
    配列aｆは参照渡しなのでa自身が変化する（ソートされる）
    """
    cnt = 0
    for i in range(n):
        flag = 0
        minj = i
        for j in range(i+1,n):
            if int(a[j][1]) < int(a[minj][1]):
                minj = j
                flag = 1
        if flag == 1:
            temp = a[minj]
            a[minj] = a[i]
            a[i] = temp
            cnt += 1
    return cnt

def bubble(a, n):
    cnt = 0
    for i in range(n):
        for j in reversed(range(i+1,n)):
            if int(a[j][1]) < int(a[j-1][1]):
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
                cnt += 1
    return cnt

def print_array(a):
    ans = str(a[0])
    for i in range(1,n):
        ans += ' '+str(a[i])  
    print(ans)

def is_stable(a, b):
    for card1 in range(len(a)):
        for card2 in range(card1+1,len(a)):
            if a[card1][1] == a[card2][1]:
                if b.index(a[card1]) > b.index(a[card2]):
                    return 'Not stable'
    return 'Stable'

n = int(input())
a = input().split()

bub = a[:]
cnt = bubble(bub, n)   
print_array(bub)
print(is_stable(a, bub))

sel = a[:]
cnt = selection(sel, n)   
print_array(sel)
print(is_stable(a, sel))
