import sys
input = sys.stdin.readline
def marge(A, left, right, mid):
    cnt = 0
    n1 = mid - left
    n2 = right - mid
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    L[n1] = 10 ** 9 + 1
    R[n2] = 10 ** 9 + 1
    i = 0
    j = 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return cnt
def margesort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        cnt1 = margesort(A, left, mid)
        cnt2 = margesort(A, mid, right)
        return cnt1 + cnt2 + marge(A, left, right, mid)
    return 0

def main():
    n = int(input())
    A = list(map(int, input().split()))
    cnt = margesort(A, 0, n)
    print(' '.join(list(map(str, A))))
    print(cnt)

if __name__ == '__main__': main()
