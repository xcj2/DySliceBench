import copy
def p(a):
    for i in a[:-1]:
        print(i,end=' ')
    print(a[-1])


def selection_sort(a):
    cnt = 0
    for i in range(len(a)-1):
        fl = 0
        min = i
        for j in range(i+1,len(a)):
            if a[j][1]<a[min][1]:
                fl=1
                min = j
        cnt+=fl
        tmp = a[min]
        a[min] = a[i]
        a[i] = tmp


def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a))[::-1]:
            if a[j-1][1]>a[j][1]:
                tmp = a[j]
                a[j] = a[j-1]
                a[j-1] = tmp


n = int(input())
l = list(input().split())
a = copy.copy(l)
bubble_sort(l)
selection_sort(a)
p(l)
print('Stable')
p(a)
if a==l:
    print('Stable')
else:
    print('Not stable')
