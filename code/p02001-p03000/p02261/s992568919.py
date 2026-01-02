import copy

class Cards:
    value = 0
    suit = ""

    def __init__(self,su,val):
        self.suit = su
        self.value = val
    
    def __str__(self):
        return f"{self.suit}{self.value}"

    def __eq__(self,other):
        if not isinstance(other, Cards):
            return NotImplemented
        
        return self.value == other.value and self.suit == other.suit


def cards_stablesort(C):
    lst = copy.deepcopy(C)
    n = len(lst)
    for i in range(1,n):
        j = i
        while(j > 0):
            if lst[j-1].value > lst[j].value:
                lst[j-1],lst[j] = lst[j],lst[j-1] #SWAP
                j -= 1
            else:
                break

    return lst

def cards_bubblesort(C):
    lst = copy.deepcopy(C)
    n = len(lst)

    for i in range(n):
        for j in range(n-1,i,-1):
            if lst[j].value < lst[j-1].value:
                lst[j],lst[j-1] = lst[j-1],lst[j]

    return lst

def cards_selectionsort(C):
    lst = copy.deepcopy(C)
    n = len(lst)

    for i in range(n):
        minj = i

        for j in range(i,n):

            if lst[j].value < lst[minj].value:
                minj = j
        
        lst[i],lst[minj] = lst[minj],lst[i]

    return lst
    


n = int(input())

l = input().split()

C = []
for cd in l:
    C.append(Cards(cd[:1],int(cd[1:])))

stable_list = cards_stablesort(C)
bubble_list = cards_bubblesort(C)
select_list = cards_selectionsort(C)

print(*bubble_list)

if stable_list == bubble_list:
    print("Stable")
else:
    print("Not stable")

print(*select_list)

if stable_list == select_list:
    print("Stable")
else:
    print("Not stable")



