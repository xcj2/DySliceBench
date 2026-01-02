MAX = 1000000001

def merge(A, left, mid, right, cnt):
    n1 = mid - left
    n2 = right - mid
    L = A[left:mid]
    R = A[mid:right]
    ls = len(L)
    L.append(MAX)
    R.append(MAX)
    
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            cnt += ls - i
            j = j + 1
    return cnt

def mergeSort(A, left, right, cnt):
    if left + 1 < right:
        mid = int((left + right) / 2)
        cnt = mergeSort(A, left, mid, cnt)
        cnt = mergeSort(A, mid, right, cnt)
        cnt = merge(A, left, mid, right, cnt)
    return cnt

def main():
    """ ????????? """
    num = int(input().strip())
    A = list(map(int,input().split()))
#    print(A)
    cnt = mergeSort(A, 0, num, 0)
    print(cnt)

if __name__ == '__main__':
    main()