a=[]
N = int(input())
for i in range(N):
    a.append(int(input()))
a=sorted(a)

if(len(a)==2):
    print(abs(a[0]-a[1]))
elif(len(a)==3):
    print(max(a[2] - a[1] + a[2] - a[0], a[1]-a[0] + a[2]-a[0]))
else:
    #----------------------------------------------------------------------
    def append2big(id1, id2):
        global bBeg
        global bEnd
        global s
        if (a[id1] - bBeg + a[id2] - bEnd < a[id2] - bBeg + a[id1] - bEnd):
            id1, id2 = id2, id1
        s+=a[id1] - bBeg + a[id2] - bEnd
        bBeg = a[id1]
        bEnd = a[id2]
    def append2small(id1, id2):
        global bBeg
        global bEnd
        global s
        if (bBeg - a[id1] + bEnd - a[id2] < bBeg - a[id2] + bEnd - a[id1]):
            id1, id2 = id2, id1
        s+=bBeg - a[id1] + bEnd - a[id2]
        bBeg = a[id1]
        bEnd = a[id2]
    def append1small(id):
        global bBeg
        global bEnd
        global s
        if (bBeg - a[id] > bEnd - a[id]):
            s+=bBeg-a[id]
            bBeg = a[id]
        else:
            s+=bEnd-a[id]
            bEnd = a[id]
    def append1big(id):
        global bBeg
        global bEnd
        global s
        if (a[id] - bBeg > a[id] - bEnd):
            s+=a[id]-bBeg
            bBeg = a[id]
        else:
            s+=a[id]-bEnd
            bEnd = a[id]
    # ----------------------------------------------------------------------
    s = a[N-2]-a[0] + a[N-1] - a[0]
    bBeg = a[N-2]
    bEnd = a[N-1]
    l = 0
    r = N-2
    cur = 0
    while(l<r-1):
        if(cur==0):
            if(l+2<r):
                append2small(l+1, l+2)
                l+=2
            elif(l+1<r):
                append1small(l+1)
                l+=1
            cur = 1-cur
        else:
            if(r-2>l):
                append2big(r-1, r-2)
                r-=2
            elif(r-1>l):
                append1big(r-1)
                r-=1
            cur = 1- cur
    r1 = s
    #-----case 2------
    s = a[N - 1] - a[0] + a[N - 1] - a[1]
    bBeg = a[0]
    bEnd = a[1]
    l = 1
    r = N - 1
    cur = 1
    while (l < r - 1):
        if (cur == 0):
            if (l + 2 < r):
                append2small(l + 1, l + 2)
                l += 2
            elif (l + 1 < r):
                append1small(l + 1)
                l += 1
            cur = 1 - cur
        else:
            if (r - 2 > l):
                append2big(r - 1, r - 2)
                r -= 2
            elif (r - 1 > l):
                append1big(r - 1)
                r -= 1
            cur = 1 - cur
    r2 = s

    print(max(r1, r2))