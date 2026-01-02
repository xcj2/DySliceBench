import time
import copy

def BubbleSort(A, N):
    flag = 1
    while flag:
        flag = 0
        for j in reversed(range(1, N)):
            if A[j]['value']<A[j-1]['value']:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1
    return A

def SelectionSort(A, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j]['value']<A[minj]['value']:
                minj = j
        if i!=minj:
            A[i], A[minj] = A[minj], A[i]
    return A

def IsStable(answer, target):
    N = len(answer)
    for i in range(N):
        if answer[i]['body'] != target[i]['body']:
            return False
    return True

# Stable Sort
def main():
    N = int(input())
    A = list(
        map(lambda x: {'body': x, 'value': int(x[1])}, input().split())
    )
    A_sortby_bubble = copy.deepcopy(A)
    A_sortby_select = copy.deepcopy(A)
    A_sortby_bubble = BubbleSort(A_sortby_bubble, N)
    A_sortby_select = SelectionSort(A_sortby_select, N)
    print(' '.join(map(lambda x: x['body'],A_sortby_bubble)))
    print('Stable')
    print(' '.join(map(lambda x: x['body'], A_sortby_select)))
    if IsStable(A_sortby_bubble, A_sortby_select):
        print('Stable')
    else:
        print('Not stable') 
    
main()
