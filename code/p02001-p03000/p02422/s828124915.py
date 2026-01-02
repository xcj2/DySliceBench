# coding: utf-8
# Your code here!

def replace_(x,y,target,replace):
    return target[:x]+replace+target[y+1:]

def reverse_(x,y,target):
    temp_rev = target[x:y+1]
    rev = temp_rev[::-1]
    return target[:x]+rev+target[y+1:]

def print_(x,y,target):
    print(target[x:y+1])


target = input()
num = int(input())
for _ in range(num):
    i = input().split()
    if i[0] == 'replace':
        target = replace_(int(i[1]),int(i[2]),target,i[3])
    elif i[0] == 'reverse':
        target = reverse_(int(i[1]),int(i[2]),target)
    elif i[0] == 'print':
        print_(int(i[1]),int(i[2]),target)

