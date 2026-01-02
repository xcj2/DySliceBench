def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def merge(A, left, right, mid):
    lstl = [[A[i][0], A[i][1]] for i in range(left, mid) ] + [[None, 1000000000]]
    lstr = [[A[i][0], A[i][1]] for i in range(mid, right)] + [[None, 1000000000]]
    pl = 0
    pr = 0
    for _ in range(left, right):
        if lstl[pl][1] <= lstr[pr][1]:
            A[left + pl + pr] = lstl[pl]
            pl += 1
        else:
            A[left + pr + pl] = lstr[pr]
            pr += 1

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, right, mid)


import sys
input = sys.stdin.readline

n = int(input())
A_q = []
A_m = []
for _ in range(n):
    card = input().split()
    A_q.append([card[0], int(card[1])])
    A_m.append([card[0], int(card[1])])

quick_sort(A_q, 0, n-1)
merge_sort(A_m, 0, n)

if A_q == A_m:
    print("Stable")
else:
    print("Not stable")

for i in range(n):
    print(" ".join(map(str, A_q[i])))
    #print(" ".join(map(str, A_m[i])))
