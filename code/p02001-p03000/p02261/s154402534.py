N = int(input())
C = [ x for x in input().split()]
C1 = C.copy()
C2 = C.copy()

def bubble_sort(N, C1):
    for i in range(N):
        for j in range(N-1, i, -1):
            if C1[j][1] < C1[j-1][1]: #2個目のカッコで文字数を指定(0スタート)
                C1[j], C1[j-1] = C1[j-1], C1[j]
    print(' '.join(map(str, C1)))   

def selection_sort(N, C2):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C2[minj][1] > C2[j][1]:
                minj = j
        C2[i],C2[minj] = C2[minj],C2[i]

    print(' '.join(map(str, C2)))


#愚直な判定
def bubble(N, C, C1):
    while True:        
        for i in range(N-1):
            for j in range(i+1, N):
                for a in range(N-1):
                    for b in range(a+1, N):
                        if C[i][1] == C[j][1] and C[i] == C1[b] and C[j] == C1[a]:
                            print('Not stable')
                            return False                            
        print('Stable')
        break

def selection(N, C, C2):
    while True:        
        for i in range(N-1):
            for j in range(i+1, N):
                for a in range(N-1):
                    for b in range(a+1, N):
                        if C[i][1] == C[j][1] and C[i] == C2[b] and C[j] == C2[a]:
                            print('Not stable')
                            return False                            
        print('Stable')
        break


bubble_sort(N, C1)
bubble(N, C, C1)
selection_sort(N, C2) 
selection(N, C, C2)                       

