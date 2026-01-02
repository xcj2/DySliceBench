# #バブルソート
# def BubbleSort(C,N):
#     for i in range (0,N,1):
#         for j in range(N-1,i-1,-1):
#             if int(C[j][1:2]) < int(C[j-1][1:2]):
#                 tmp = C[j]
#                 C[j] = C[j-1]
#                 C[j-1] = tmp
#     print(' '.join(C))

#バブルソート
def BubbleSort(C,N):
    flag = 1
    while flag:
        flag = 0
        for j in range(N-1,0,-1):
            if int(C[j][1:2]) < int(C[j-1][1:2]):
                tmp = C[j]
                C[j] = C[j-1]
                C[j-1] = tmp
                flag = 1
    print(' '.join(C))
    
    
                
                
#選択ソート
def SelectionSort(C,N):
    for i in range(0,N,1):
        minj = i
        for j in range(i,N,1):
            if int(C[j][1:2]) < int(C[minj][1:2]):
                minj = j
        tmp = C[i]
        C[i] = C[minj]
        C[minj] = tmp
    print(' '.join(C))
        
#安定かどうかの判定
def isStable(inp, out,N):
    for i in range(0,N):
        for j in range(i+1,N):
            for a in range(0,N):
                for b in range(a+1,N):
#                     print("inp(i,j):",inp[i],inp[j],"out(b,a):",out[b],out[a]+"\n")
                    if int(inp[i][1]) == int(inp[j][1]) and inp[i] == out[b] and inp[j] == out[a]:
                        print('Not stable')
                        return
    print('Stable')


#愚直に調べるパターン
N = int(input())
A = list(input().split())
Bubble_A = A.copy()
Selection_A = A.copy()

BubbleSort(Bubble_A,N)
isStable(A,Bubble_A,N)
SelectionSort(Selection_A,N)
isStable(A,Selection_A,N)
