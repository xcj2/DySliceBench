N = int(input())
card_list_source = input().split(' ')

def BubbleSort(card_list, N):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if int(card_list[j][1]) < int(card_list[j-1][1]):
                temp = card_list[j]
                card_list[j] = card_list[j-1]
                card_list[j-1] = temp
    return card_list

def SelectionSort(card_list, N):
    for i in range(N):
        min_index = i
        for j in range(i+1, N):
            if int(card_list[j][1]) < int(card_list[min_index][1]):
                min_index = j
        if min_index != i:
            temp = card_list[i]
            card_list[i] = card_list[min_index]
            card_list[min_index] = temp
    return card_list

def isStable(card_list_A, card_list_B):
    N = len(card_list_A)
    for i in range(N):
        for j in range(i+1, N):
            for a in range(N):
                for b in range(a+1, N):
                    if int(card_list_A[i][1]) == int(card_list_A[j][1]) and card_list_A[i] == card_list_B[b] and card_list_A[j] == card_list_B[a]:
                        return 'Not stable'
    return 'Stable'

def make_out_str(card_list):
    out_str = ''
    for i, card in enumerate(card_list):
        out_str += card
        if i < len(card_list) - 1:
            out_str += ' '
    return out_str

card_list_bubble = BubbleSort(card_list_source.copy(), N)
print(make_out_str(card_list_bubble))
print(isStable(card_list_bubble, card_list_source))

card_list_selection = SelectionSort(card_list_source.copy(), N)
print(make_out_str(card_list_selection))
print(isStable(card_list_selection, card_list_source))



