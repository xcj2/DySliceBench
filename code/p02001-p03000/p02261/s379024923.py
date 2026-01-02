import copy

def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j]['value'] < A[j-1]['value']:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp


def selection_sort(B):
    for i in range(len(B)):
        mini = i
        for j in range(i, len(B)):
            if B[j]['value'] < B[mini]['value']:
                mini = j
        tmp = B[i]
        B[i] = B[mini]
        B[mini] = tmp


def is_stable(A, B, n):
    for i in range(n):
        if A[i]['suit'] != B[i]['suit']:
            return False
    return True


def show_list(C):
    D = [i['suit'] + i['value'] for i in C]
    print(' '.join(D))
    
n = int(input())
A = [{'suit': i[0], 'value': i[-1]}for i in map(str, input().split())]
B = copy.deepcopy(A)

bubble_sort(A)
show_list(A)
print('Stable')

selection_sort(B)
show_list(B)
if is_stable(A, B, n):
    print('Stable')
else:
    print('Not stable')
