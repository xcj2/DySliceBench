import copy
n=int(input())
a=list(input().split())
def BubbleSort(l,n):
    a=copy.deepcopy(l)
    for i in range(n):
        for j in reversed(range(i+1,n)):
            if int(a[j][1])<int(a[j-1][1]):
                a[j],a[j-1]=a[j-1],a[j]
    return a

def SelectionSort(l,n):
    a=copy.deepcopy(l)
    for i in range(n):
        minj=i
        for j in range(i,n):
            if int(a[j][1])<int(a[minj][1]):
                minj=j
        a[i],a[minj]=a[minj],a[i]
    return a

def SP(l):
    for i in range(len(l)):
        if i !=len(l)-1:
            print(l[i],end=' ')
        else:
            print(l[i]) 

BS=BubbleSort(a,n)
SS=SelectionSort(a,n)
SP(BS)
print('Stable')
SP(SS)
if BS==SS:
    print('Stable')
else:
    print('Not stable')
