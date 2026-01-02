from sys import stdin
N = int(input())
A = [{'value': int(x[1]), 'type': x[0]} for x in stdin.readline().split(' ')]
S = 'Stable'
NS = 'Not stable'


def bubble_sort(arr):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if arr[j]['value'] < arr[j - 1]['value']:
                arr[j], arr[j - 1] = (arr[j - 1], arr[j])
    return arr


def selection_sort(arr):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if arr[j]['value'] < arr[minj]['value']:
                minj = j
        arr[i], arr[minj] = (arr[minj], arr[i])
    return arr


A_bubble = bubble_sort(A.copy())
A_selection = selection_sort(A.copy())


def is_stable(origin, arr):
    for i in range(N):
        for j in range(i+1, N):
            for a in range(0, N):
                for b in range(a+1, N):
                    if (arr[i]['value'] == arr[j]['value']) & \
                            (arr[i] == origin[b]) & (arr[j] == origin[a]):
                        return False

    return True


print(' '.join(map(lambda x: x['type'] + str(x['value']), A_bubble)))
print(S)

print(' '.join(map(lambda x: x['type'] + str(x['value']), A_selection)))
if (is_stable(A_bubble, A_selection)):
    print(S)
else:
    print(NS)

