def getval():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    a.sort()
    b.sort()
    c.sort()
    return n,a,b,c 

def main(n,a,b,c):
    def bs(arr,key):
        lo = 0
        hi = len(arr)-1
        while lo<=hi:
            idx = (lo+hi)//2
            if arr[idx]>=key:
                hi = idx-1
            else:
                lo = idx+1
        return hi

    arrb = []
    arrc = []
    for i in b:
        arrb.append(bs(a,i)+1)
    for i in c:
        arrc.append(bs(b,i)+1)
    for i in range(1,n):
        arrb[i] += arrb[i-1]
    ans = 0
    for i in arrc:
        if i!=0:
            ans += arrb[i-1]
    print(ans)

if __name__=="__main__":
    n,a,b,c = getval()
    main(n,a,b,c)