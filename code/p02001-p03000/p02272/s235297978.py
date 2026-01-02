from bisect import bisect_right as br
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def MergeSort(aa, left=0, right=-1):
    def merge(aa, left2, mid2, right2):
        res=0
        inf = float("inf")
        L = aa[left2:mid2] + [inf]
        R = aa[mid2:right2] + [inf]
        Li = Ri = 0
        for ai in range(left2, right2):
            res+=1
            if L[Li] < R[Ri]:
                aa[ai] = L[Li]
                Li += 1
            else:
                aa[ai] = R[Ri]
                Ri += 1
        return res

    res=0
    if right == -1: right = len(aa)
    if left + 1 < right:
        mid = (left + right) // 2
        res+=MergeSort(aa, left, mid)
        res+=MergeSort(aa, mid, right)
        res+=merge(aa, left, mid, right)
    return res

def main():
    n=int(input())
    aa=list(map(int, input().split()))
    cnt=MergeSort(aa)
    print(*aa)
    print(cnt)
main()

