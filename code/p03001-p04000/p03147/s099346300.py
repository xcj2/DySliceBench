# C
def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]
N = getInt()
h = getIntList()
count = 0
def water(r,l):
    global count
    #print(r,l,h,count)#
    mn = min(h[r:l])
    count += mn
    for i in range(r,l):
        h[i] -= mn
    i = r
    #print(r,l,h,count)#
    while i<l:
        #print('i',i)#
        if h[i]>0:
            j = i+1
            #print('j',j)#
            while j<=l:
                #print(j)#
                if j>=l or h[j]==0:
                    water(i,j)
                    break
                j += 1
            i = j
        i += 1
water(0,N)
print(count)