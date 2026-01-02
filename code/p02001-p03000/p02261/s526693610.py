class Card(object):
    def __init__(self, card):
        self._suit = card[0]
        self._value = int(card[1])

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__ == other.__dict__

    def getValue(self):
        return self._value

    def toString(self):
        return self._suit + str(self._value)


def card_bubbleSort(lst, n):
    for i in range(0, n):
        for j in range(n-1, i, -1):
            if lst[j].getValue() < lst[j-1].getValue():
                tmp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = tmp

    return lst


def card_selectionSort(lst, n):
    for i in range(0, n):
        minj = i
        for j in range(i, n):
            if lst[j].getValue() < lst[minj].getValue():
                minj = j

        if i != minj:
            tmp = lst[i]
            lst[i] = lst[minj]
            lst[minj] = tmp

    return lst


def isStable(in_lst, out_lst, n):
    for i in range(0, n):
        for j in range(i+1, n):
            for a in range(0, n):
                for b in range(a+1, n):
                    if in_lst[i].getValue() == in_lst[j].getValue() \
                            and in_lst[i] == out_lst[b] \
                            and in_lst[j] == out_lst[a]:
                                return False
    return True


if __name__ == "__main__":
    n = int(input())
    lst = input().split()
    func_table = [card_bubbleSort, card_selectionSort]
    for func in func_table:
        cards = [Card(item) for item in lst]
        result = func(cards, n)
        cards = [Card(item) for item in lst]
        print(" ".join([card.toString() for card in result]))
        if isStable(cards, result, n):
            print("Stable")
        else:
            print("Not stable")