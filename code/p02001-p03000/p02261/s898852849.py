def is_stable(bubble, selection, _N):
    for i in range(N):
        if bubble[i][0] != selection[i][0]:
            return False
    return True


def bubble(N_input, A_input):
    count = 0
    flag = 1
    _A = list(A_input)

    while flag:
        flag = 0
        for i in range(N_input-1, 0, -1):
            _A_i = int(_A[i][1])
            _A_i_1 = int(_A[i-1][1])

            if _A_i < _A_i_1:
                _A[i], _A[i-1] = _A[i-1], _A[i]

                flag = 1
                count += 1

    return _A


def selection(inN, inA):
    _A = list(inA)

    for i in range(0, inN-1, 1):
        minj = i
        for j in range(i+1, inN, 1):
            if int(_A[j][1]) < int(_A[minj][1]):
                minj = j
        _A[i], _A[minj] = _A[minj], _A[i]

    return _A


N = int(input())
# A = list(map(int, input().split()))
A = input().split()
# print(N, A)

A_bubble = bubble(N, A)
A_bubble_str = map(str, A_bubble)
print(' '.join(A_bubble_str))
print('Stable')

A_selection = selection(N, A)
A_selection_str = map(str, A_selection)
print(' '.join(A_selection_str))
if is_stable(A_bubble, A_selection, N):
    print('Stable')
else:
    print('Not stable')

