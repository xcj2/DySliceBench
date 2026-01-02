import copy


# global
cards_origin = []


# function
def BubbleSort(count, cards):
    for i in range(count):
        for j in range(count-1, i, -1):
            if cards[j][1] < cards[j-1][1]:
                cards[j], cards[j-1] = cards[j-1], cards[j]


def SelectionSort(count, cards):
    for i in range(count):
        minj = i
        for j in range(i, count):
            if cards[j][1] < cards[minj][1]:
                minj = j
        cards[i], cards[minj] = cards[minj], cards[i]
        

def SuitOrder(cards, numbers):
    for i in range(len(cards)):
        numbers[cards[i][1]].append(cards[i][0])


def IsStable(numbers1, numbers2):
    for i in range(len(numbers1)):
        if numbers1[i] != numbers2[i]:
            return "Not stable"

    return "Stable"



if __name__ == "__main__":

    # 入力
    in_count = int(input())
    in_cards = input().split(" ")

    # 入力されたカードの値を独自の配列に格納 ["suit", number]
    for i in range(in_count):
        cards_origin.append([in_cards[i][0], int(in_cards[i][1])])

    # リストをコピーしておく
    cards_bubble = copy.deepcopy(cards_origin)
    cards_selection = copy.deepcopy(cards_origin)

    # 関数呼び出し
    BubbleSort(in_count, cards_bubble)
    SelectionSort(in_count, cards_selection)

    # 1から9までの数字に対し、絵柄がどの順番で出現するか求め、0-9のリストに格納
    # _originとbubble, _originとselectionでそれぞれ比較する
    order_origin = []
    order_bubble = []
    order_selection = []
    for i in range(10):
        order_origin.append([])
        order_bubble.append([])
        order_selection.append([])

    
    SuitOrder(cards_origin, order_origin)
    SuitOrder(cards_bubble, order_bubble)
    SuitOrder(cards_selection, order_selection)
    

    bubble_is_stable = IsStable(order_origin, order_bubble)
    selection_is_stable = IsStable(order_origin, order_selection)

    # 表示
    for i in range(len(cards_bubble)):
        print("%s%d" % (cards_bubble[i][0], cards_bubble[i][1]), end="")
        if i != len(cards_bubble)-1:
            print(" ", end="")
    print()
    print(bubble_is_stable)


    for i in range(len(cards_selection)):
        print("%s%d" % (cards_selection[i][0], cards_selection[i][1]), end="")
        if i != len(cards_selection)-1:
            print(" ", end="")
    print()
    print(selection_is_stable)

