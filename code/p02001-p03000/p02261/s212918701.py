# coding=utf-8

def print_list(X):
    first_flag = True
    for val in X:
        if first_flag:
            print_line = str(val)
            first_flag = False
        else:
            print_line = print_line + ' ' + str(val)
    print(print_line)

def combine_list(A_suit, A_rank, N):
    A_after = []
    for i in range(N):
        A_after.append(A_suit[i] + str(A_rank[i]))
    return A_after


def bubble_sort(A, index_list, N):
    #print_list(A)
    #flag: ???????????????????????????True???????´?
    flag = True
    i = 0
    while flag:
        flag = False
        for j in range(N-1, i, -1):
            if A[j] < A[j-1]:
                A[j-1], A[j] = A[j], A[j-1]
                index_list[j-1], index_list[j] = index_list[j], index_list[j-1]
                flag = True
        i += 1
    return A, index_list

def selection_sort(A, index_list, N):
    for i in range(N):
        min_j = i
        for j in range(i, N):
            if A[j] < A[min_j]:
                min_j = j
        if i != min_j:
            A[i], A[min_j] = A[min_j], A[i]
            index_list[i], index_list[min_j] = index_list[min_j], index_list[i]
    return A, index_list

def main():
    N = int(input())
    A = list(input().split())
    A_suit = []
    A_rank = []
    index_list = [x for x in range(N)]
    A_after_bubble = []
    A_after_selection = []

    for element in A:
        val = list(element)
        val_suit = val[0]
        val_rank = int(val[1])
        A_suit.append(val_suit)
        A_rank.append(val_rank)
    A_suit_after_bubble = [0 for x in range(N)]
    A_suit_after_selection = [0 for x in range(N)]

    A_rank_after_bubble, index_list_after_bubble = bubble_sort(A_rank.copy(), index_list.copy(), N)
    A_rank_after_selection, index_list_after_selection = selection_sort(A_rank.copy(), index_list.copy(), N)

    for index_before, index_after in enumerate(index_list_after_bubble):
        A_suit_after_bubble[index_before] = A_suit[index_after]

    for index_before, index_after in enumerate(index_list_after_selection):
        A_suit_after_selection[index_before] = A_suit[index_after]

    A_after_bubble = combine_list(A_suit_after_bubble, A_rank_after_bubble, N)
    A_after_selection = combine_list(A_suit_after_selection, A_rank_after_selection, N)

    print_list(A_after_bubble)
    print("Stable")
    print_list(A_after_selection)
    if A_after_selection == A_after_bubble:
        print("Stable")
    else:
        print("Not stable")



if __name__ == '__main__':
    main()