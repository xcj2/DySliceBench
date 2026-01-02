# coding:utf-8

s = input()
t = input()

def bSort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

    return a

def bSort2(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] > a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a


def add_list(a):
    sumed = ""
    for i in a:
        sumed += i
    return sumed

s_list = list(s)
s_ = add_list(bSort(s_list))

t_list = list(t)
t_ = add_list(bSort2(t_list))

if s_ < t_:
    print('Yes')
else:
    print('No')
