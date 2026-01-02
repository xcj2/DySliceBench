import copy

class Cards:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

def Partition(NUM_LIST, left, right):
    v = NUM_LIST[right-1].value
    border = left
    for foot in range(left, right-1):
        if NUM_LIST[foot].value <= v:
            NUM_LIST[foot], NUM_LIST[border] = NUM_LIST[border], NUM_LIST[foot]
            border += 1
    NUM_LIST[right-1], NUM_LIST[border] = NUM_LIST[border], NUM_LIST[right-1]
    return border
    
def QuickSort(NUM_LIST, left, right):
    if left+1 < right:
        q = Partition(NUM_LIST, left, right)
        QuickSort(NUM_LIST, left, q)
        QuickSort(NUM_LIST, q+1, right)

def MergeSort(NUM_LIST, left, right):
    if left+1 < right:
        mid = (left+right)//2
        MergeSort(NUM_LIST, left, mid)
        MergeSort(NUM_LIST, mid, right)
        Merge(NUM_LIST, left, mid, right)

def Merge(NUM_LIST, left, mid, right):
    L = NUM_LIST[left:mid]
    inf = Cards("inf", 1000000001)
    L.append(inf)
    R = NUM_LIST[mid:right]
    R.append(inf)
    i=0
    j=0
    for k in range(left, right):
        if L[i].value > R[j].value:
            NUM_LIST[k] = R[j]
            j += 1
        else:
            NUM_LIST[k] = L[i]
            i += 1

n = int(input())
CARD_LIST = []

for i in range(n):
    c, v = input().split()
    v = int(v)
    tmp = Cards(c, v)
    CARD_LIST.append(tmp)

QUICK_LIST = copy.copy(CARD_LIST)
MERGE_LIST = copy.copy(CARD_LIST)

QuickSort(QUICK_LIST, 0, len(QUICK_LIST))
MergeSort(MERGE_LIST, 0, len(MERGE_LIST))


if QUICK_LIST == MERGE_LIST:
    print("Stable")
else:
    print("Not stable")
    
for i in range(len(MERGE_LIST)):
    print("%s %d"%(QUICK_LIST[i].letter, QUICK_LIST[i].value))
    
    
