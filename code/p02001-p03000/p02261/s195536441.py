import copy

def bubbleSort(C, M, N):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if C[j] < C[j-1]:
                out1 = C[j]
                C[j] = C[j-1]
                C[j-1] = out1
                out2 = M[j]
                M[j] = M[j-1]
                M[j-1] = out2
    print(' '.join(M))
    print('Stable')
    return M
    
def selectionSort(C, M, N):
    m = copy.deepcopy(M)
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j] < C[minj]:
                minj = j
        out3 = C[i]
        C[i] = C[minj]
        C[minj] = out3
        out4 = M[i]
        M[i] = M[minj]
        M[minj] = out4
    print(' '.join(M))
    return M
    
def isStable(inn, out):
    for a, b in zip(inn, out):
        if a == b: continue
        else : return 'Not stable'
    return 'Stable'
    
if __name__ == '__main__':
    num1 = []
    N = int(input()) #1行目のNを取得する
    M1 = list(input().split())
    for i in range(N):
        s = M1[i]
        num1.append(int(s[-1]))
    M2 = copy.deepcopy(M1)
    num2 = copy.deepcopy(num1)
    out1 = bubbleSort(num1, M1, N)
    out2 = selectionSort(num2, M2, N)
    print(isStable(out1, out2))
