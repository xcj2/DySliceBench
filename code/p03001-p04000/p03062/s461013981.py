N = int(input())
A = [int(x) for x in input().split()]

def count_negative(A):
    count = 0
    for i in range(len(A)):
        if A[i] < 0:
            count += 1
    return count

def find_zero(A):
    for i in range(len(A)):
        if A[i] == 0:
            return True
    return False

def even(x):
    if x % 2 == 0:
        return True
    return False

def flipping_signs(A):
    A_abs = [abs(x) for x in A]
    sum_A_abs = sum(A_abs)
    if even(count_negative(A)) or find_zero(A):
        print(sum_A_abs)
    else:
        A_abs_min = min(A_abs)
        print(sum_A_abs - 2 * A_abs_min)

flipping_signs(A)