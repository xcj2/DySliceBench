"""
クイックソート

6
D 3
H 2
D 1
S 3
D 2
C 1
"""
import copy

MAX = 500000
L = [None] * int(MAX / 2 + 2) 
R = [None] * int(MAX / 2 + 2) 
# 番兵
SENTINEL = "2000000000000"
from pprint import pprint

def quick_sort(A, n, p, r):
    if p < r:
        q = partition(A, n, p, r)
        # pprint(A)
        # z = []
        # for a in A:
        #     z.append(a.mark_num)
        # print(z)
        quick_sort(A, n, p, q-1)
        quick_sort(A, n, q+1, r)

def partition(A, n, p, r):
    # print(n, p, r)
    x = A[r].num
    i = p
    # print(p)
    for k in range(p, r+1):
        if A[k].num <= x:
            tmp = A[i]
            A[i] = A[k]
            A[k] = tmp
            i += 1
            # print(i)
    return i-1

def merge(B, n, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    for i in range(n1):
        L[i] = B[left + i]
    for i in range(n2):
        R[i] = B[mid + i]
    L[n1] = Card("dummy {}".format(SENTINEL))
    R[n2] = Card("dummy {}".format(SENTINEL))
    i = 0
    j = 0
    k = left
    while  k < right:
        if L[i].num <= R[j].num:
            B[k] = L[i]
            i += 1
        elif L[i].num > R[j].num:
            B[k] = R[j]
            j += 1
        k += 1


def merge_sort(B, n, left, right):
    if (left+1) <  right:
        
        mid = int((left + right) / 2)
        # print(A, n, left, mid, right)
        merge_sort(B, n, left, mid)
        merge_sort(B, n, mid, right)
        merge(B, n, left, mid, right)

            

class Card:
    def __init__(self, mark_num):
        self.mark_num = mark_num
        self.num = int(mark_num.split()[1])


if __name__=="__main__":
    n = int(input())
    A = []
    for i in range(n):
        row = input()
        A.append(Card(row))

    B = copy.deepcopy(A)

    quick_sort(A, n, 0, n-1)
    # for a in A:
    #     print(a.mark_num)
    
    # print("======")
    merge_sort(B, n, 0, n)
    # for b in B:
    #     print(b.mark_num)
    # print(" ".join(A_str))

    for i in range(n):
        if A[i].mark_num != B[i].mark_num:
            print("Not stable")
            break
    else:
        print("Stable")
        # print(A[i].mark_num, B[i].mark_num)

    for a in A:
        print(a.mark_num)
    
