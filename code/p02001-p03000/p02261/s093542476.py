import copy

class Card:
    def __init__(self, mark_num):
        self.mark_num = mark_num
        self.mark = mark_num[0]
        self.num = int(mark_num[1:])

def bubble_sort(cards, n):
    flag = True
    while flag:
        flag = False
        for i in reversed(range(1, n)):
            if cards[i].num < cards[i-1].num:
                tmp = cards[i]
                cards[i] = cards[i-1]
                cards[i-1] = tmp
                flag = True
    
    # for c in cards:
    #     print(c.mark_num + " ", end="")

    mark_nums = []
    for c in cards:
        mark_nums.append(c.mark_num)

    print(" ".join(mark_nums))
    print("Stable")

    return cards

    # nums_str = map(str, nums)
    # print(" ".join(cards))
    # print(cards)

def selection_sort(cards, n):
    for i in range(n):
        minj = i
        flag = False
        for j in range(i, n-1):
            if cards[minj].num > cards[j+1].num:
                minj = j+1
                flag = True
        
        if flag:
            tmp = cards[i]
            cards[i] = cards[minj]
            cards[minj] = tmp

    mark_nums = []
    for c in cards:
        mark_nums.append(c.mark_num)

    print(" ".join(mark_nums))

    return cards

def is_stable(cards1, cards2, n):
    is_stable = True
    for i in range(n):
        if cards1[i].mark_num != cards2[i].mark_num:
            is_stable = False
            break

    if is_stable:
        print("Stable")
    else:
        print("Not stable")
    
#     nums_str = map(str, nums)
#     print(" ".join(nums_str))
#     print(count)

if __name__=="__main__":
    n = int(input())
    input_cards = list(input().split())
    card_list = []
    for input_card in input_cards:
        card = Card(input_card)
        card_list.append(card)

    cards_1 = bubble_sort(copy.deepcopy(card_list), n)
    cards_2 = selection_sort(copy.deepcopy(card_list), n)

    is_stable(cards_1, cards_2, n)

