def BobbleSort(C, N):
    flag = True
    while flag:
        flag = False
        for i in range(N-1,0,-1):
            if C[i-1][1] > C[i][1]:
                C[i-1], C[i] = C[i], C[i-1]
                flag = True
    return C

def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]

def Stable(C1, C2, N):
    # Stable なら True
    flag = True
    
    # C2 を並び替え後とする
    for i in range(1, N):
        if C2[i-1][1] == C2[i][1]:
            a = C1.index(C2[i-1])
            b = C1.index(C2[i])
            if a > b:
                flag = False
                break
    
    if flag:
        print("Stable")
    else:
        print("Not stable")
    
N = int(input())
orgC = [x for x in input().split()]
C = orgC.copy()

BobbleSort(C,N)
print(" ".join(C))
Stable(orgC, C, N)

C = orgC.copy()
SelectionSort(C,N)
print(" ".join(C))
Stable(orgC, C, N)
