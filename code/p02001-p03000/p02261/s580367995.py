#愚直な判定
def JudgeStable(inC, outC, N):
    for i in range(N):
        for j in range(i+1, N):
            for a in range(N):
                for b in range(a+1, N):
                    if inC[i][1] == inC[j][1] and inC[i] == outC[b] and inC[j] == outC[a]:
                        return False
    return True

def PrintJudge(judge):
    if judge:
        print('Stable')
    else:
        print('Not stable')
        
def BubbleSort(C, N):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if C[j-1][1] > C[j][1]:
                C[j-1], C[j] = C[j], C[j-1]
                
def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i+1, N):
            if C[minj][1] > C[j][1]:
                minj = j
        C[minj], C[i] = C[i], C[minj]
                
def PrintC(C):
    print(' '.join([''.join([c[0], str(c[1])]) for c in C]))

N = int(input())
C = [[c[0], int(c[1])] for c in input().split()]
C1 = C.copy()
C2 = C.copy()

BubbleSort(C1, N)
SelectionSort(C2, N)

PrintC(C1)
PrintJudge(JudgeStable(C, C1, N))

PrintC(C2)
PrintJudge(JudgeStable(C, C2, N))
