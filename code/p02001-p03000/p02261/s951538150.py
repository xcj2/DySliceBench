import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def SelectionSort(aa,n):
    for i in range(n):
        min_j=i
        for j in range(i+1,n):
            if int(aa[j][1])<int(aa[min_j][1]):min_j=j
        if min_j!=i:
            aa[i],aa[min_j]=aa[min_j],aa[i]
    return aa

def BubbleSort(aa,n):
    for i in range(n):
        for j in range(i,0,-1):
            if int(aa[j-1][1])<=int(aa[j][1]):break
            aa[j-1],aa[j]=aa[j],aa[j-1]
    return aa

def main():
    n = int(input())
    #aa = list(map(int, input().split()))
    aa=input().split()
    atoi={}
    for i,a in enumerate(aa):
        atoi[a]=i

    sorted_aa=BubbleSort(aa[:],n)
    stable=True
    for a0,a1 in zip(sorted_aa,sorted_aa[1:]):
        if a0[1]==a1[1] and atoi[a0]>atoi[a1]:
            stable=False
    print(*sorted_aa)
    print("Stable") if stable else print("Not stable")

    sorted_aa=SelectionSort(aa[:],n)
    stable=True
    for a0,a1 in zip(sorted_aa,sorted_aa[1:]):
        if a0[1]==a1[1] and atoi[a0]>atoi[a1]:
            stable=False
    print(*sorted_aa)
    print("Stable") if stable else print("Not stable")

main()

