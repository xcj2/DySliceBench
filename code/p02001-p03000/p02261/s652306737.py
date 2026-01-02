# ALDS1_2_C: Stable Sort
N = int(input())
A = input().split()

#N = 5
#A = "H4 C9 S4 D2 C3".split()

#N = 2
#A = "S1 H1".split()

def insertionSort(A, N):
    #print(" ".join(map(str, A)))
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and int(A[j][1]) > int(v[1]):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = v
    #print(" ".join(map(str, A)))
    return " ".join(map(str, A))
    
stablesort = insertionSort(A.copy(), N)

def bubbleSort(A, N):
    flag = True
    i = 0
    while(flag):
        flag = False
        for j in reversed(range(1, N)):
            if int(A[j][1]) < int(A[j-1][1]):                
                A[j], A[j-1] = A[j-1], A[j]
                flag = True
                i += 1
                #print(A)
    print(" ".join(map(str, A)))
    #print(i)
    return " ".join(map(str, A))
    
bubble = bubbleSort(A.copy(), N)
if bubble == stablesort:
    print("Stable")
else:
    print("Not stable")

def selectionSort(A, N):
    e = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
            e += 1
            #print(A)
    print(" ".join(map(str, A)))
    #print(e)
    return " ".join(map(str, A))
    
selection = selectionSort(A.copy(), N)
if selection == stablesort:
    print("Stable")
else:
    print("Not stable")

