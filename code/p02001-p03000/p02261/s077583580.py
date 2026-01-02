def bubbleSort(a, n):   #n個の要素を持つ配列a
    flag = 1    #逆の隣接要素あり
    i = 0       #未ソートの先頭
    #count = 0
    while flag:
        flag = 0
        for j in range(n-1, i, -1): #j n-1...i+1
            if a[j][1] < a[j-1][1]:

                a[j], a[j-1] = a[j-1], a[j]
                #count += 1
                flag = 1
        i += 1
    print(' '.join(map(str, a)))
    #print(count)

def selectionSort(a, n):
    #count = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j][1] < a[minj][1]:
                minj = j
        a[i], a[minj] = a[minj], a[i]
    printArray(a)
    #print(count)

def isStable(a1, a2):
    if a1 == a2:
        print("Stable")
    else:
        print("Not stable")


#配列の出力
def printArray(a):
    print(' '.join(map(str, a)))

#配列の要素数と要素の入力
n = int(input())
a = list(input().split())
a2 = a.copy()

bubbleSort(a, n)
print("Stable")
selectionSort(a2, n)
isStable(a, a2)
