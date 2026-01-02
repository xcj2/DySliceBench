INF = int(1e9)
def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    n = len(A)
    L = A[left:mid] + [INF] 
    R = A[mid:right] + [INF]
    i = 0
    j = 0
    cnt = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
            cnt = cnt + n1 - i
    return cnt

def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left+right)//2
        cnt1 = mergeSort(A, left, mid)
        cnt2 = mergeSort(A, mid, right)
        cnt3 = merge(A, left, mid, right)
        return (cnt1 + cnt2 + cnt3)
    else: 
        return 0

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = mergeSort(a, 0, n)
    print(ans)
main()
