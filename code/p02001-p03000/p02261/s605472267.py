def bubbleSort(A,N):
    flag = 1
    sortedIndex = 0
    i = 0
    while flag == 1:
        flag = 0
        for j in range(N-1,sortedIndex,-1):
            if int(A[j][1]) < int(A[j-1][1]):
                v = A[j]
                A[j] = A[j-1]
                A[j-1] = v
                flag = 1
                i += 1

def selectionSort(A,N):
    for i in range(N):
        minj = i
        for j in range(i+1,N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        v = A[i]
        A[i] = A[minj]
        A[minj] = v

def isStable(before,after,N):
    for i in range(N):
        for j in range(i+1,N):
            for a in range(N):
                for b in range(a+1,N):
                    if before[i][1] == before[j][1] and before[i] == after[b] and before[j] == after[a]:
                        #print("i={} j={} a={} b={}".format(i,j,a,b))
                        return False
    return True

def bubble_is_stable(A,N):
    bubble = A.copy()
    bubbleSort(bubble,N)
    bubble_is_stable = isStable(A,bubble,N)
    bubblestr = ''
    for i in range(N):
        bubblestr += "{} ".format(bubble[i])
    print(bubblestr[:len(bubblestr)-1])
    if bubble_is_stable:
        print('Stable')
    else:
        print('Not stable')

def selection_is_stable(A,N):
    selection = A.copy()
    selectionSort(selection,N)
    selection_is_stable = isStable(A,selection,N)
    selectionstr = ''
    for i in range(N):
        selectionstr += "{} ".format(selection[i])
    print(selectionstr[:len(selectionstr)-1])
    if selection_is_stable:
        print('Stable')
    else:
        print('Not stable')

if __name__ == '__main__':
    N = int(input())
    A = [ _ for _ in input().split()]
    bubble_is_stable(A,N)
    selection_is_stable(A,N)

