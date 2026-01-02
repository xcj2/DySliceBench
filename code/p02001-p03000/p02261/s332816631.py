import copy

N = int(input())
A = list(input().split())

def is_stable(sorted_list):
    for i in range(len(sorted_list)-1):
        if sorted_list[i][1] == sorted_list[i+1][1]:
            for j in range(len(A)):
                if A[j] == sorted_list[i]:
                    smaller_idx = j
                if A[j] == sorted_list[i+1]:
                    larger_idx = j
            if smaller_idx > larger_idx:
                return False
    return True

def print_stable_or_not(is_stable):
    if is_stable:
        print("Stable")
    else:
        print("Not stable")

def bubble_sort(A1):
    flg = True
    while flg:
        for i in range(N):
            flg = False
            for j in range(N-1, i, -1):
                if int(A1[j-1][1]) > int(A1[j][1]):
                    A1[j-1], A1[j] = A1[j], A1[j-1]
                    flg = True
    print(" ".join(A1))
    print_stable_or_not(is_stable(A1))

def insertion_sort(A2):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if int(A2[min_idx][1]) > int(A2[j][1]):
                min_idx = j
        if min_idx != i:
            A2[i], A2[min_idx] = A2[min_idx], A2[i]
    print(" ".join(A2))
    print_stable_or_not(is_stable(A2))

if __name__ == '__main__':
    A1 = copy.deepcopy(A)
    A2 = copy.deepcopy(A)
    bubble_sort(A1)
    insertion_sort(A2)
