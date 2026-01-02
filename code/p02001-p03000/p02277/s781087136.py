n = int(input())
cards = []
for i in range(n):
    sign, num = input().split(' ')
    cards.append((int(num), sign))

#in: A list of (num, sign) p:start r:end
#out: return i+1
def partition(A, p, r):
    pivot = A[r][0]
    i = p-1
    for j in range(p, r):
        if A[j][0]<= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

#in: list of (num, sign)
#out: none  overwrite list
def quick_sort(cards, p, r):
    if p >= r:
        return
    pivot = partition(cards, p, r)
    quick_sort(cards, p, pivot-1)
    quick_sort(cards, pivot+1, r)

def merge(list1, list2):
    output = []
    p1 = 0
    p2 = 0
    l1 = len(list1)
    l2 = len(list2)
    while p1 < l1 and p2 < l2:
        if list1[p1][0] <= list2[p2][0]:
            output.append(list1[p1])
            p1 += 1
        else:
            output.append(list2[p2])
            p2 += 1
    return output + list1[p1:] + list2[p2:]

#in: A list of (num, sign)
#out: none overwrite
def merge_sort(cards):
    if len(cards) <= 1:
        return cards
    else:
        pivot = len(cards)//2
        return merge(merge_sort(cards[:pivot]), merge_sort(cards[pivot:]))
        
quick = cards.copy()
quick_sort(quick, 0, len(quick)-1)
merge = merge_sort(cards)

for i in range(n):
    if quick[i][1] != merge[i][1]:
        print("Not stable")
        break
else:
    print("Stable")

for num, sign in quick:
    print( sign + ' ' + str(num))
