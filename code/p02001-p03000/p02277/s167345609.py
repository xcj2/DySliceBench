import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def QuickSort(aa, p, r):
    def Partition(aa, p, r):
        x = aa[r][0]
        i = p - 1
        for j in range(p, r):
            if aa[j][0] <= x:
                i += 1
                aa[i], aa[j] = aa[j], aa[i]
        aa[i + 1], aa[r] = aa[r], aa[i + 1]
        return i + 1

    if p < r:
        q = Partition(aa, p, r)
        QuickSort(aa, p, q - 1)
        QuickSort(aa, q + 1, r)

def main():
    n = int(input())
    #aa = list(map(int, input().split()))
    cc=[]
    ctoi={}
    for i in range(n):
        m,a=input().split()
        c=(int(a),m)
        ctoi[c]=i
        cc.append(c)
    QuickSort(cc,0,n-1)
    stable=True
    for c0,c1 in zip(cc,cc[1:]):
        if c0[0]==c1[0] and ctoi[c0]>ctoi[c1]:
            stable=False
            break
    print("Stable") if stable else print("Not stable")
    for c in cc:
        print(c[1],c[0])

main()

