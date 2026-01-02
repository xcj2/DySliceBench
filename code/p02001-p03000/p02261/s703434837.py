import copy


def bubbleSort(sort_list, N):

    before = copy.deepcopy(sort_list)

    for i in range(0, N):
        for j in range(N - 1, i, -1):
            if int(sort_list[j][1]) < int(sort_list[j - 1][1]):
                tmp = sort_list[j]
                sort_list[j] = sort_list[j - 1]
                sort_list[j - 1] = tmp

    print(' '.join(sort_list))
    print(checkStable(before, sort_list))


def selectionSort(sort_list, N):
    before = copy.deepcopy(sort_list)

    for i in range(0, N):
        minj = i

        for j in range(i, N):
            if int(sort_list[j][1]) < int(sort_list[minj][1]):
                minj = j

        if minj != i:
            tmp = sort_list[i]
            sort_list[i] = sort_list[minj]
            sort_list[minj] = tmp

    print(' '.join([str(i) for i in sort_list]))
    print(checkStable(before, sort_list))


def checkStable(before_list, sorted_list):

    for val in sorted_list:
        same_list = [
            i for i in sorted_list if (int(val[1]) == int(i[1])) and val != i
        ]
        if len(same_list) == 0:
            continue

        for data in same_list:
            bef = before_list.index(val) - before_list.index(data)
            aft = sorted_list.index(val) - sorted_list.index(data)

            if (bef > 0 and aft < 0) or (bef < 0 and aft > 0):
                return 'Not stable'

    return 'Stable'


if __name__ == "__main__":
    N = int(input())
    sort_list = input().split()

    sort_list2 = copy.deepcopy(sort_list)
    bubbleSort(sort_list, N)
    selectionSort(sort_list2, N)

