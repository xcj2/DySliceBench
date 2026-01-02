import sys, copy
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
    A = []
    for _ in range(n):
        SN = LSS()
        A.append((SN[0], int(SN[1])))

    A_org = copy.deepcopy(A)

    def partition(A, p, r):
        x = A[r][1]
        i = p-1
        for j in range(p, r):
            if A[j][1]<=x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    def quickSort(A, p, r):
        if p<r:
            q = partition(A, p, r)
            quickSort(A, p, q-1)
            quickSort(A, q+1, r)

    def is_stable(A, A_org):
        # 数字をkey、スート列をvalueに持つ辞書を使って比較

        d_A = {}
        for i in A:
            if i[1] in d_A:
                d_A[i[1]].append(i[0])
            else:
                d_A[i[1]] = [i[0]]
        d_A_org = {}
        for i in A_org:
            if i[1] in d_A_org:
                d_A_org[i[1]].append(i[0])
            else:
                d_A_org[i[1]] = [i[0]]

        if d_A == d_A_org:
            return 'Stable'
        else:
            return 'Not stable'

    quickSort(A, 0, n-1)
    print(is_stable(A, A_org))
    for s, n in A:
        print(s, n)

if __name__ == '__main__':
    resolve()

