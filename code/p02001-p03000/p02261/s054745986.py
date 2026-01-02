def bubbleSort(C, N):
    for i in range(0, N):
        for j in range(N-1, i, -1):
            if C[j][1]<C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]
    return C
 
def selectionSort(C, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C
 
def check(C0, C1):
    for i in range(N):
        for j in range(i+1, N):
            for a in range(N):
                for b in range(a+1, N):
                    if C0[i][1] == C0[j][1] and C0[i] == C1[b] and C0[j] == C1[a]:
                        return False
    return True
 
def toStr(a):
    return str(a[0])+str(a[1])
 
N = int(input())
src = [(str(char[0]), int(char[1])) for char in input().split()]
 
out_1 = bubbleSort(src[:], N)
out_2 = selectionSort(src[:], N)
# &は2進数
# リストは参照渡し
for out in [out_1, out_2]:
    ans = map(toStr, out)
    print(*ans)
    if check(src, out):
        print('Stable')
    else:
        print('Not stable')
