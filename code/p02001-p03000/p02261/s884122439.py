import copy


class Card :
        def __init__(self, char, num) :
                self.text = char
                self.value = num


def bubble_sort(Card, n) :
    for i in range(n) :
        for j in reversed(range(i+1, n)) :
            if Card[j].value < Card[j-1].value :
                Card[j], Card[j-1] = Card[j-1], Card[j]


def selection_sort(Card, n) :
    for i in range(n) :
        minj = i
        for j in range(i, n) :
            if Card[j].value < Card[minj].value :
                minj = j
        Card[i], Card[minj] = Card[minj], Card[i]


def is_stable(lst_bubble, lst_sel) :
    for i in range(len(lst_bubble)) :
        if lst_bubble[i].text != lst_sel[i].text :
            return False
    return True


def print_result(lst, n) :
    for i in range(n-1) :
        print(lst[i].text + str(lst[i].value), end = "")
        print(" ", end = "")
    print(lst[-1].text + str(lst[-1].value))


def main() :
    n = int(input())
    lst1 = input().split()
    card_list1 = []
    for i in range(n) :
        card = Card(lst1[i][0], int(lst1[i][1]))
        card_list1.append(card)

    card_list2 = copy.deepcopy(card_list1)

    bubble_sort(card_list1, n)
    selection_sort(card_list2, n)

    print_result(card_list1, n)
    print("Stable")
    print_result(card_list2, n)
    if (is_stable(card_list1, card_list2)) :
        print("Stable")
    else :
        print("Not stable")


if __name__ == '__main__' :
        main()