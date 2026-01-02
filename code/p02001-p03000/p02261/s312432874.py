# Algorithms and Data Structures 1
# Stable Sort
# Name: Ryuya Asada
# ID: s1260064


def BubbleSort(A: list):
    flag = 1
    while flag:
        flag = 0
        for j in range(len(A)-1, 0, -1):
            if A[j][1] < A[j-1][1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1


def SelectionSort(A: list):
    for i in range(0, len(A)):
        minj = i
        for j in range(i, len(A)):
            if A[j][1] < A[minj][1]:
                minj = j

        A[i], A[minj] = A[minj], A[i]


def isEqual(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False

    elif a == []:
        return True

    return (a.pop() == b.pop()) and isEqual(a, b)


def main():
    number_of_cards = int(input())
    cards = input().split(" ")

    cards_b = cards.copy()
    BubbleSort(cards_b)
    print(*cards_b, sep=" ")
    print("Stable")
    cards_s = cards.copy()
    SelectionSort(cards_s)
    print(*cards_s, sep=" ")
    if isEqual(cards_b, cards_s):
        print("Stable")
    else:
        print("Not stable")
    pass


if __name__ == "__main__":
    main()

