def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


def merge(A, left, mid, right):
    global Comp_count
    n1 = mid - left
    n2 = right - mid
    L = A[left:mid]
    R = A[mid:right]
    L.append(1000000001)
    R.append(1000000001)
    i = 0  # L[]??¨?????????????????????
    j = 0  # R[]??¨?????????????????????
    for k in range(left, right):
        Comp_count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


from array import array
def merge_with_array(A, left, mid, right):
    global Comp_count
    n1 = mid - left
    n2 = right - mid
    L = array('I', A[left:mid])
    R = array('I', A[mid:right])
    L.append(1000000001)
    R.append(1000000001)

    i = 0  # L[]??¨?????????????????????
    j = 0  # R[]??¨?????????????????????
    for k in range(left, right):
        Comp_count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

from ctypes import *
class DATA(Structure):
    _fields_ = ("d", c_int * 250002),
L = DATA()
R = DATA()

def merge_with_ctypes(A, left, mid, right):
    global Comp_count
    n1 = mid - left
    n2 = right - mid
    for i in range(n1):
        L.d[i] = A[left+i]
    for i in range(n2):
        R.d[i] = A[mid+i]
    L.d[n1] = 1000000001
    R.d[n2] = 1000000001

    i = 0  # L[]??¨?????????????????????
    j = 0  # R[]??¨?????????????????????
    for k in range(left, right):
        Comp_count += 1
        if L.d[i] <= R.d[j]:
            A[k] = L.d[i]
            i += 1
        else:
            A[k] = R.d[j]
            j += 1



Comp_count = 0
if __name__ == '__main__':
    # ??????????????\???
    num_of_data = int(input())
    S = [int(x) for x in input().split(' ')]
    #with open('ALDS1_5_B_in10.txt') as f:
    #    for line in f:
    #        if ' ' not in line:
    #            num_of_data = int(line)
    #        else:
    #            S = [int(x) for x in line.split(' ')]
    #S = [8, 5, 9, 2, 6, 3, 7, 1, 10, 4]

    # ????????????????????????
    merge_sort(S, 0, num_of_data)

    # ???????????????
    print('{0}'.format(' '.join(map(str, S))))
    print(Comp_count)