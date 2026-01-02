import sys
import copy
input = sys.stdin.readline


def main():
    N = int(input())
    P = list(input().split())
    bubbleSortted = bubbleSort(N, copy.copy(P))
    print(' '.join(map(str, bubbleSortted)))
    print("Stable")
    selectionSorted = selectionSort(N, copy.copy(P))
    print(' '.join(map(str, selectionSorted)))
    print(isStable(bubbleSortted, selectionSorted))


def selectionSort(N, P):
    change_count = 0
    for i in range(0, N):
        minj = i

        # print(P[i:N])
        # print(min(P[i:N]))

        for j in range(i, N):
            if P[j][1] < P[minj][1]:
                minj = j

        if i != minj:
            tmp = P[i]
            P[i] = P[minj]
            P[minj] = tmp
            change_count += 1

        # print(' '.join(map(str, P)))

    return P


def bubbleSort(N, P):
    change_count = 0
    i = 0
    while True:
        for j in range(N - 1, i, -1):
            if P[j][1] < P[j - 1][1]:
                tmp = P[j]
                P[j] = P[j - 1]
                P[j - 1] = tmp
                change_count += 1
        i += 1
        # print("i:{}".format(i))
        if i == N:
            break

    return P


def isStable(P1, P2):
    for i in range(len(P1)):
        # print("P1:{0},P2:{1}".format(P1[i], P2[i]))
        if P1[i] != P2[i]:
            return "Not stable"
    return "Stable"


if __name__ == '__main__':
    main()

