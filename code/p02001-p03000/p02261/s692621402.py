def val(a):
    return int(a[1:])


def bubble(lst,n):
    for i in range(n):
        for j in range(n-1,i,-1):
            if val(lst[j])<val(lst[j-1]):
                lst[j],lst[j-1]=lst[j-1],lst[j]
    return lst

def selection(lst,n):
    for i in range(n):
        minj=i
        for j in range(i,n):
            if val(lst[j])<val(lst[minj]):
                minj=j
        if i!=minj:
            lst[minj],lst[i]=lst[i],lst[minj]
    return lst

n=int(input())
lst=input().split()
lstc=lst[:]
blst=bubble(lstc,n)
lstc=lst[:]
slst=selection(lstc,n)


print(" ".join(blst))
print("Stable") #バブルソートは安定ソート
print(" ".join(slst))
if slst==blst : print("Stable")
else : print("Not stable")
