def getInput():
    n = int(input())
    a = [i for i in input().split(" ")]
    return n, a

def getNum(s):
    return int(s[1])

def swap(x, y):
    v = x
    x = y
    y = v
    return x, y

def bubbleSort(n, a):
    cnt = 0
    for j in range(n):
        init = True
        for i in range(n-1, -1, -1):
            if init:
                init = False
                continue
            if getNum(a[i]) > getNum(a[i+1]):
                a[i], a[i+1] = swap(a[i], a[i+1])
                cnt += 1
    print(" ".join([str(i) for i in a]))
    return a

def selectionSort(n, a):
    cnt = 0
    for i in range(n):
        id_min = i
        for j in range(i+1, n):
            if getNum(a[j]) < getNum(a[id_min]):
                id_min = j
        if id_min != i:
            a[i], a[id_min] = swap(a[i], a[id_min])
            cnt += 1
    print(" ".join([str(i) for i in a]))
    return a

def checkStability(n, a_sample, a):
    for i in range(n-1):
        flag1 = False
        flag2 = False
        if getNum(a_sample[i]) == getNum(a_sample[i+1]):
            for j in range(n):
                if a[j] == a_sample[i+1]:
                    flag1 = True
                if a[j] == a_sample[i]:
                    flag2 = True
                if (flag1==True)&(flag2==False):
                    print("Not stable")
                    return
    print("Stable")
    return


from copy import deepcopy
N, A = getInput()
a_bs = bubbleSort(deepcopy(N), deepcopy(A))
checkStability(deepcopy(N), deepcopy(a_bs), deepcopy(A))
a_ss = selectionSort(deepcopy(N), deepcopy(A))
checkStability(deepcopy(N), deepcopy(a_ss), deepcopy(A))

