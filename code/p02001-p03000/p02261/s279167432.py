from copy import copy


def bubble_sort(C, N):
    for i in range(N):
        for j in reversed(range(i + 1, N)):
            if int(C[j][1]) < int(C[j - 1][1]):
                C[j - 1], C[j] = C[j], C[j - 1]
    return C


def selection_sort(C, N):
    for i in range(N):
        minj = i
        for j in range(i+1, N):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C


def to_dict(C):
    dictionary = {n: [] for n in range(1, 36+1)}
    for card in C:
        m, i = tuple(card)
        dictionary[int(i)].append(m)
    return dictionary


N = int(input())
* C, = input().split()
C_dict = to_dict(C)
BC = bubble_sort(copy(C), N)
BC_dict = to_dict(BC)
SC = selection_sort(copy(C), N)
SC_dict = to_dict(SC)

print(*BC)
if C_dict == BC_dict:
    print('Stable')
else:
    print('Not Stable')
print(*SC)
if C_dict == SC_dict:
    print('Stable')
else:
    print('Not stable')

