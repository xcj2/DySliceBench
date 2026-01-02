import copy


class Card:
    def __init__(self, mark, number):
        self.mark = mark
        self.number = number

    def __repr__(self):
        return self.mark + str(self.number)


def bubble_sort(C, N):
    for i in range(N):
        for j in range(i + 1, N)[::-1]:
            if C[j-1].number > C[j].number:
                C[j-1], C[j] = C[j], C[j-1]


def selection_sort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j].number < C[minj].number:
                minj = j
        C[i], C[minj] = C[minj], C[i]


if __name__ == "__main__":
    N = int(input())
    C_raw = list(input().split())
    C = []
    for i in range(N):
        c = Card(C_raw[i][0], int(C_raw[i][1]))
        C.append(c)

    C_for_bubble = copy.copy(C)
    bubble_sort(C_for_bubble, N)
    print(' '.join(map(str, C_for_bubble)))
    print('Stable')

    C_for_selection = copy.copy(C)
    selection_sort(C_for_selection, N)
    print(' '.join(map(str, C_for_selection)))
    if C_for_bubble == C_for_selection:
        print('Stable')
    else:
        print('Not stable')

