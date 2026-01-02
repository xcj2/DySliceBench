import copy
def BubbleSort(C, N):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if C[j][1:2] <  C[j-1][1:2]:
                C[j], C[j-1] = C[j-1], C[j]

    print(*C)
    stableCheck(C, N)

def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1:2] <  C[minj][1:2]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    print(*C)
    stableCheck(C, N)

def stableCheck(C, N):
    global lst
    flag = 1
    for i in range(N):
        for j in range(i+1, N):
            if lst[i][1:2] == lst[j][1:2]:
                fir = lst[i]
                sec = lst[j]
                for k in range(N):
                    if C[k] == fir:
                        recf = k

                    if C[k] == sec:
                        recs = k
                
                if recf > recs:
                    print("Not stable")
                    flag = 0
                    break
        
        if flag ==0:
            break

    if flag :
        print("Stable")

N = int(input())
lst = list(map(str, input().split()))
lst1 = copy.deepcopy(lst)
lst2 = copy.deepcopy(lst)

BubbleSort(lst1, N)
SelectionSort(lst2, N)
