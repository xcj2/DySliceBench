# coding=utf-8

def partition(A, p, r):
    x = A[r][1]
    i = p-1
    for j in range(p, r):
        if A[j][1] <= x:
            A[i+1], A[j] = A[j], A[i+1]
            i += 1
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def is_stable(A):
    for i in range(len(A) - 1):
        if A[i][1] == A[i+1][1]:
            if A[i][2] > A[i+1][2]:
                return False
    return True


n = int(input())
cards = []
for i in range(n):
    suit, num = input().split()
    cards.append([suit, int(num), i])

quick_sort(cards, 0, n-1)

if is_stable(cards):
    print("Stable")
else:
    print("Not stable")

for i in range(n):
    print(cards[i][0], cards[i][1])