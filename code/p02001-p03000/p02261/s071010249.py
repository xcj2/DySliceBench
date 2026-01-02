import sys

def selection_sort(n, A):
    for i in range(n-1):
        minj = i
        for j in range(i+1,n):
            if A[minj][1:] > A[j][1:]:
                minj = j

        A[i], A[minj] = A[minj], A[i]
    return A

def bubble_sort(n, A):

    for i in range(n):
        for j in range(n-1, i, -1):
            if A[j-1][1:] > A[j][1:]:
                A[j], A[j-1] = A[j-1], A[j]
    return A

def is_stable(in_data, out_data):
    len_data = len(in_data)

    for i in range(len_data):
        for j in range(i+1, len_data):
            for a in range(len_data):
                for b in range(a+1, len_data):
                    if in_data[i][1] == in_data[j][1] and\
                       in_data[i] == out_data[b] and\
                       in_data[j] == out_data[a]:
                        return False

    return True

n = int(sys.stdin.readline().strip())
card = sys.stdin.readline().strip().split(' ')

raw = card[:]
bs = bubble_sort(n, raw)
raw = card[:]
ss = selection_sort(n, raw)

print(' '.join(bs))

if is_stable(card, bs):
    print('Stable')
else:
    print('Not stable')

print(' '.join(ss))

if is_stable(card, ss):
    print('Stable')
else:
    print('Not stable')

