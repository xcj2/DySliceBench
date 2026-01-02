from copy import deepcopy


def printer(A):
    ret = str(A[0][1]) + str(A[0][0])
    for i in range(1, len(A)):
        ret += " " + str(A[i][1]) + str(A[i][0])
    print(ret)
    return True


def devide(card):
    ret = []
    for c in card:
        num = int(c[1])
        pic = c[0]
        ret.append((num, pic))
    return ret


def bubblesort(A):
    ret = 0
    flag = True
    num = len(A)
    while flag is True:
        flag = False
        for i in reversed(range(1, num)):
            if A[i - 1][0] > A[i][0]:
                tmp = A[i - 1]
                A[i - 1] = A[i]
                A[i] = tmp
                flag = True
                ret += 1
                # print(A)
        # num -= 1
    return ret


def selection_sort(A):
    ans = 0
    for i in range(len(A)):
        minj = i
        for j in range(i, len(A)):
            if A[minj][0] > A[j][0]:
                minj = j
        if i != minj:
            ans += 1
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp
    return ans


def isStable(card, sorted_card):
    if len(card) != len(sorted_card):
        return False
    for i in range(len(card)):
        c = card[i]
        s = sorted_card[i]
        if c[0] != s[0] or c[1] != s[1]:
            return False
    return True


n = int(input())
card = list(map(str, input().split()))

card = devide(card)
card_bubble = deepcopy(card)
card_selection = deepcopy(card)

bubblesort(card_bubble)
selection_sort(card_selection)

# print(card_bubble)
printer(card_bubble)
print("Stable")

printer(card_selection)
if isStable(card_bubble, card_selection) is True:
    print("Stable")
else:
    print("Not stable")
