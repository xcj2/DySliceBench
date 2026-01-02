# coding: utf-8
# Here your code !
A = int(input())
N = tuple(input().split())
bs=[]
ss=[]
def isStable(a,b):
    leng = int(len(a))
    for i in range(leng):
        for j in range(i+1,leng):
            for x in range(leng):
                for y in range(x+1,leng):
                    if a[i][1]==a[j][1] and a[i]==b[y] and a[j]==b[x]:
                        return "Not stable"
    return "Stable"
    
def bSort(n,a):
    n = list(n)
    for i in range(a):
        for j in range(a-1,i,-1):
            if int(n[j][1]) < int(n[j-1][1]):
                n[j],n[j-1]=n[j-1],n[j]
    return n
    #print(" ".join(n))

    
def seleSort(n,a):
    n = list(n)
    for i in range(a):
        minj = i
        for j in range(i+1,a):
            if n[j][1]<n[minj][1]:
                minj = j
                
        n[i],n[minj]=n[minj],n[i]
    return n
    #print(" ".join(n))

bs = bSort(N,A)
ss = seleSort(N,A)
print(" ".join(bs))
print(isStable(bs,bs))
print(" ".join(ss))
print(isStable(bs,ss))