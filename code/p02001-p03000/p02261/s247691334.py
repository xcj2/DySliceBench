import copy
class Card:
    def __init__(self, str):
        self.mark = str[0]
        self.number = int(str[1:])
        
    def __str__(self):
        return self.mark + str(self.number)
        
n = int(input())
card_list = [Card(c) for c in input().split()]

def bubble_sort(a):
    a = copy.copy(a)
    n = len(a)
    for i in range(n):
            for j in range(0, n-i-1):
                if a[j].number > a[j+1].number:
                    a[j], a[j+1] = a[j+1], a[j]
    return a
    
sorted_card_list1 = bubble_sort(card_list)
print(*sorted_card_list1)
print("Stable")

def selection_sort(a):
    a = copy.copy(a)
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if a[j].number < a[min_index].number:
                min_index = j
        if i != min_index:
            a[i],a[min_index] = a[min_index],a[i]
    return a

    
sorted_card_list2 = selection_sort(card_list)
print(*sorted_card_list2)
if sorted_card_list1 == sorted_card_list2:
    print("Stable")
else:
    print("Not stable")
