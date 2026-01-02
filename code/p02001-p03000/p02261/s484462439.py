class Card:
    __slots__ = ["mark", "value"]

    def __init__(self, text):
        self.mark = text[0]
        self.value = int(text[1])

    def __str__(self):
        return f"{self.mark}{self.value}"


def BubbleSort(lst):
    lst = lst.copy()
    for i in range(0, len(lst)):
        for j in range(len(lst) - 1, i, -1):
            if lst[j].value < lst[j -1].value:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst


def SelectionSort(lst):
    lst = lst.copy()
    for i in range(0, len(lst)):
        minj = i
        for j in range(i, len(lst)):
            if lst[j].value < lst[minj].value:
                minj = j
        lst[i], lst[minj] = lst[minj], lst[i]
    return lst

def check_stable(lst):
    for x in range(1, 10):
        if "".join(c.mark for c in lst if c.value == x) != "".join(c.mark for c in C if c.value == x):
            return False
    return True


input()
C = [Card(i) for i in input().split()]
B = BubbleSort(C)
S = SelectionSort(C)
print(" ".join(map(str, B)))
print("Stable" if check_stable(B) else "Not stable")
print(" ".join(map(str, S)))
print("Stable" if check_stable(S) else "Not stable")

