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
    H = I()
    A = [0]
    tmp = LI()
    for i in tmp:
        A.append(i)

    def maxHeapify(A, i):
        l = 2*i
        r = 2*i+1
        if l <= H and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r <= H and A[r] > A[largest]:
            largest = r

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            maxHeapify(A, largest)

    def buildMaxHeap(A):
        for i in range(H//2, 0, -1):
            maxHeapify(A, i)

    buildMaxHeap(A)

    ans = ''
    for i in range(1, H+1):
        ans += ' ' + str(A[i])
    print(ans)

if __name__ == '__main__':
    resolve()

