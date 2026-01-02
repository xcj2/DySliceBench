def number_of_inv(A, n):
    cnt = 0

    def merge(A, left, mid, right):
        L = A[left:mid]
        R = A[mid:right]
        n = right - left
        n1 = mid - left
        C = [0] * n
        L.append(float('inf'))
        R.append(float('inf'))
        i = 0
        j = 0
        nonlocal cnt
        for k in range(left, right):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                cnt += n1 - i
                j += 1
        return cnt

    def merge_sort(A, left, right):
        if left+1 < right:
            mid = (left + right) >> 1
            merge_sort(A, left, mid)
            merge_sort(A, mid, right)
            return merge(A, left, mid, right)
    
    if len(A) == 1:
        return 0
    else:
        return merge_sort(A, 0, n)

n = int(input())
A = [int(i) for i in input().split()]
print(number_of_inv(A, n))
