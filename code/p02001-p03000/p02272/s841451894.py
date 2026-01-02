import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n = I()
    S = LI()

    cnt = [0]

    def merge(A, left, mid, right):
        L = A[left:mid]
        R = A[mid:right]
        L.append(INF)
        R.append(INF)
        i = 0
        j = 0
        for k in range(left, right):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            cnt[0] += 1

    def mergeSort(A, left, right):
        if left+1 < right:
            mid = (left+right)//2
            mergeSort(A, left, mid)
            mergeSort(A, mid, right)
            merge(A, left, mid, right)

    mergeSort(S, 0, n)
    print(*S)
    print(cnt[0])

if __name__ == '__main__':
    resolve()
