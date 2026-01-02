from typing import List


def bubble_sort(elems: List[str]) -> List[str]:
    for i in range(0, len(elems)):
        for j in range(len(elems) - 1, i, -1):
            if int(elems[j][1]) < int(elems[j - 1][1]):
                elems[j], elems[j - 1] = elems[j - 1], elems[j]
    return elems


def selection_sort(elems: List[str]) -> List[str]:
    for i in range(0, len(elems)):
        mini = i
        for j in range(i + 1, len(elems)):
            if int(elems[j][1]) < int(elems[mini][1]):
                mini = j
        if i != mini:
            elems[i], elems[mini] = elems[mini], elems[i]
    return elems


def is_stable(input_elems: List[str], elems: List[str]) -> bool:
    for card1, card2 in zip(elems[:-1], elems[1:]):
        if (int(card1[1]) == int(card2[1])) and (
           input_elems.index(card1) > input_elems.index(card2)):
            return False
    return True


if __name__ == "__main__":
    elem_num = int(input())
    elems = list(input().split())

    elems_bubble_sort = elems.copy()
    elems_bubble_sort = bubble_sort(elems_bubble_sort)
    print(" ".join(elems_bubble_sort))
    if is_stable(elems, elems_bubble_sort):
        print("Stable")
    else:
        print("Not stable")

    elems_selection_sort = elems.copy()
    elems_selection_sort = selection_sort(elems_selection_sort)
    print(" ".join(elems_selection_sort))
    if is_stable(elems, elems_selection_sort):
        print("Stable")
    else:
        print("Not stable")

