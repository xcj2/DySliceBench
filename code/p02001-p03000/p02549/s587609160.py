def pointUpdate(BIT,index,val):
    mod = 998244353
    while index < len(BIT):
        BIT[index] += val
        BIT[index] %= mod
        index += index&-index

def pointQuery(BIT,index):
    mod = 998244353
    total = 0
    while index > 0:
        total += BIT[index]
        index -= index&-index
        total %= mod

    return total

def rangeUpdate(BIT,l,r,val):
    pointUpdate(BIT,l,val)
    pointUpdate(BIT,r+1,-val)

def main():
    n,k = map(int,input().split())
    segs = []
    for i in range(k):
        l,r = map(int,input().split())
        segs.append((l,r))

    segs.sort()

    mod = 998244353
    BIT = [0]*(n+1)
    BIT[1] = 1
    for cell in range(1,n+1):
        curr = pointQuery(BIT,cell)
        if cell == n:
            print(curr)
        for l,r in segs:
            left = min(cell+l,n+1)
            right = min(cell+r,n+1)
            rangeUpdate(BIT,left,right,curr)

main()
