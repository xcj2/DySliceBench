from copy import deepcopy

N = int(input())
oary = input().split()


def bubble_sort(ary):
    for i in range(N):

        for j in range(N - 1, i, -1):
            if int(ary[j][1:]) < int(ary[j - 1][1:]):
                ary[j], ary[j - 1] = ary[j - 1], ary[j]


def selection_sort(ary):

    for i in range(0, N):
        minj = i

        for j in range(i, N):
            if int(ary[j][1:]) < int(ary[minj][1:]):
                minj = j

        ary[i], ary[minj] = ary[minj], ary[i]


def naive_check(oary, nary):
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            for a in range(1, N - 1):
                for b in range(a + 1, N):

                    if int(oary[i][1:]) == int(nary[j][1:]):
                        if oary[i] == nary[b]:
                            if oary[j] == nary[a]:
                                return False

    return True


def is_stable(oary, nary):

    if naive_check(oary, nary):
        print('Stable')
    else:
        print('Not stable')


bary = deepcopy(oary)
bubble_sort(bary)
print(' '.join(bary))
print('Stable')
# is_stable(oary, bary)

sary = deepcopy(oary)
selection_sort(sary)
print(' '.join(sary))
if bary == sary:
    print('Stable')
else:
    print('Not stable')
# is_stable(oary, sary)

