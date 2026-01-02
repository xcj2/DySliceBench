import copy
import sys
input = sys.stdin.readline


def bubble_sort(A):
    for _ in range(len(A)):
        for i in range(1, len(A))[::-1]:
            if int(A[i][1:]) < int(A[i - 1][1:]):
                A[i], A[i - 1] = A[i - 1], A[i]
    return A


def selection_sort(A):
    for i in range(len(A)):
        _min = i
        for j in range(i, len(A)):
            if int(A[j][1:]) < int(A[_min][1:]):
                _min = j
        A[i], A[_min] = A[_min], A[i]
    return A


def main():
    _ = input()
    A = input().strip().split()
    b_A = copy.deepcopy(A)
    bubble_sort(b_A)
    print(" ".join(b_A))
    print("Stable")

    selection_sort(A)
    print(" ".join(A))
    for b, s in zip(b_A, A):
        if b == s:
            continue
        else:
            print("Not stable")
            return
    print("Stable")
    return


if __name__ == "__main__":
    main()

