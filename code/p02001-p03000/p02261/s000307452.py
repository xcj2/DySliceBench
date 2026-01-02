def bubbleSort(c, n):
    flag = 1
    while(flag) :
        flag = 0
        for i in reversed(range(1,n)):
            if(c[i][1] < c[i-1][1]):
                c[i], c[i-1] = c[i-1], c[i]
                flag = 1
    return c

def selectionSort(c,n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if(c[j][1] < c[minj][1]):
                minj = j
        c[i], c[minj] = c[minj], c[i]
    return c

def isStable(c1, c2, n):
    for i in range(n):
        if(c1[i] != c2[i]):
            return False
    return True

n = int(input())
c = input().split(' ')
trump = [list(i) for i in c]
bubble = ["".join(s) for s in bubbleSort(trump, n)]
trump = [list(i) for i in c]
selection = ["".join(s) for s in selectionSort(trump, n)]
str_bubble = " ".join(bubble)
str_selection = " ".join(selection)
print(str_bubble)
print('Stable')
print(str_selection)
if isStable(bubble, selection, n):
    print('Stable')
else:
    print('Not stable')

