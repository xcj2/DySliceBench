from typing import List


def bubble_sort(A: List[str], N: int) -> List[str]:
    for i in range(N - 1):
        for j in range(N - 1, i, -1):
            if A[j - 1][1] > A[j][1]:
                A[j - 1], A[j] = A[j], A[j - 1]
    return A


def selection_sort(A: List[str], N: int) -> List[str]:
    for i in range(N - 1):
        tmp_min_index: int = i
        for j in range(i + 1, N):
            if A[tmp_min_index][1] > A[j][1]:
                tmp_min_index = j
        A[i], A[tmp_min_index] = A[tmp_min_index], A[i]
    return A


def is_stable(A: List[str], A_sorted: List[str], N: int) -> bool:
    for i in range(N - 1):
        for j in range(i + 1, N):
            # for a in range(N - 1):
            #     for b in range(a + 1, N):
            #         if A[i][1] == A[j][1] and A_sorted[a] == A[j] and A_sorted[b] == A[i]:
            #             return False
            if A[i][1] == A[j][1] and A_sorted.index(A[j]) < A_sorted.index(A[i]):
                return False
    return True


def main():
    N: int = int(input())
    A: List[str] = list(input().split())

    A_bubble = bubble_sort(A[:], N)
    A_selection = selection_sort(A[:], N)

    print(*A_bubble, sep=" ")
    print("Stable")
    print(*A_selection, sep=" ")
    print("Stable") if A_bubble == A_selection else print("Not stable")

    # print("Stable") if is_stable(A, A_bubble,
    #                              N) else print("Not stable")
    # print("Stable") if is_stable(A, A_selection,
    #                              N) else print("Not stable")


if __name__ == "__main__":
    main()

