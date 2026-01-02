import sys


def partition_for_second_element(array, first, end):
    criteria = array[end][1]
    i_ins = first
    for i_cur in range(first, end):
        if array[i_cur][1] <= criteria:
            array[i_ins], array[i_cur] = array[i_cur], array[i_ins]     # swap
            i_ins += 1
    array[i_ins], array[end] = array[end], array[i_ins]     # swap
    return i_ins


def quick_sort(array, first, end):
    #print("quick_sort",first,end,array)
    if first < end:
        criteria_idx = partition_for_second_element(array, first, end)
        quick_sort(array, first, criteria_idx - 1)
        quick_sort(array, criteria_idx + 1, end)


def shcd_order(cards):
    orders = {}
    for card in cards:
        if card[1] not in orders:
            orders[card[1]] = [card[0]]
        else:
            orders[card[1]].append(card[0])
    return orders


def is_identical_order(prev_orders, after_orders):
    for key, value in prev_orders.items():
        if after_orders[key] != value:
            return False
    return True


def main():
    input_lines = sys.stdin.readlines()
    n = int(input_lines[0].rstrip())
    cards = [(x.split()[0], int(x.split()[1])) for x in input_lines[1:]]
    prev_orders = shcd_order(cards)
    quick_sort(cards, 0, n-1)
    after_orders = shcd_order(cards)
    if is_identical_order(prev_orders, after_orders):
        print('Stable')
    else:
        print('Not stable')
    [print(x[0], x[1]) for x in cards]
    return


main()
