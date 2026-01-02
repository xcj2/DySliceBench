import sys

ERROR_INPUT = 'input is invalid'


def main():
    n = get_length()
    arr = get_array(length=n)

    bubbleLi = bubbleSort(li=arr.copy(), length=n)
    selectionLi = selectionSort(li=arr.copy(), length=n)

    print(*list(map(lambda c: c.card, bubbleLi)))
    print(checkStable(inp=arr, out=bubbleLi))
    print(*list(map(lambda c: c.card, selectionLi)))
    print(checkStable(inp=arr, out=selectionLi))
    return 0


def get_length():
    n = int(input())
    if n < 1 or n > 36:
        print(ERROR_INPUT)
        sys.exit(1)
    else:
        return n


def get_array(length):
    nums = input().split(' ')
    return [Card(n) for n in nums]


def bubbleSort(li, length):
    for n in range(length):
        for n in range(1, length - n):
            if li[n].num < li[n - 1].num:
                li[n], li[n - 1] = li[n - 1], li[n]

    return li


def selectionSort(li, length):
    for i in range(0, length - 1):
        min_index = i
        for j in range(i, length):
            if li[j].num < li[min_index].num:
                min_index = j

        if i != min_index:
            li[i], li[min_index] = li[min_index], li[i]

    return li


def checkStable(inp, out):
    small_num = out[0].num

    for n in range(1, len(out)):
        if out[n].num == small_num:
            if inp.index(out[n]) < inp.index(out[n - 1]):
                return 'Not stable'
        elif small_num < out[n].num:
            small_num = out[n].num
            continue

    return 'Stable'


class Card:
    def __init__(self, disp):
        li = list(disp)
        self.card = disp
        self.chara = li[0]
        self.num = int(li[1])
        return


main()