import sys
from copy import deepcopy
input = sys.stdin.readline

def partition(p, r):
    x = int(A[r][1])
    i = p
    for j in range(p, r):
        if int(A[j][1]) <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

def quick_sort(p, r):
    if p < r:
        q = partition(p, r)
        quick_sort(p, q-1)
        quick_sort(q+1, r)

def is_stable(original_list, sorted_list):
    for key, val in sorted_list:
        for original_key, original_val in original_list[:]:
            if val == original_val:
                if key != original_key:
                    print("Not stable")
                    return
                original_list.remove([original_key, original_val])
                break
    print("Stable")
    return
    
if __name__ == "__main__":
    n = int(input())
    A = [input().split() for _ in range(n)]
    A_original = deepcopy(A)
    quick_sort(0, n-1)
    is_stable(A_original, A)
    for key, val in A:
        print("{} {}".format(key, val))
