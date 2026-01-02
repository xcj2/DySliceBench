# coding: utf-8
# Your code here!
INF = 10**10

def merge(A, l, mid, r):
    a1 = A[l:mid] + [[None, INF]]
    a2 = A[mid:r] + [[None, INF]]
    i = j = 0
    for k in range(l, r):
        if a1[i][1] <= a2[j][1]:
            A[k] = a1[i]
            i += 1
        else:
            A[k] = a2[j]
            j += 1

def merge_sort(A, l, r):
    if l + 1 >= r:
        return
    mid = (l + r) // 2
    
    merge_sort(A, l, mid)
    merge_sort(A, mid, r)
    
    merge(A, l, mid, r)
    
    
def quick_sort(A, l, r):
    if l < r:
        #mid = (l + r) // 2
        mid = r
        pivot = A[mid][1]
        A[mid], A[r] = A[r], A[mid]
        i = 0
        for j in range(l, r):
            if A[j][1] <= pivot:
                A[l+i], A[j] = A[j], A[l+i]
                i += 1
        A[l+i], A[r] = A[r], A[l+i]
        
        quick_sort(A, l, l+i-1)
        quick_sort(A, l+i+1, r)

n = int(input())
cards = [input().split() for _ in range(n)]

for card in cards:
    card[1] = int(card[1])

confirm_cards  = cards[:]

quick_sort(cards, 0, n - 1)
merge_sort(confirm_cards, 0, n)

if cards == confirm_cards:
    print('Stable')
else:
    print('Not stable')
    
for card in cards:
    print(*card)

#print('-----')
#for card in confirm_cards:
#    print(*card)
    
        
