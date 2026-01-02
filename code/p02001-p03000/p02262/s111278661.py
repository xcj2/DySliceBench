n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

def insertionSort(l,n,g):
    cnt=0
    for i in range(g,n):
        v=l[i]
        j=i-g
        while j>=0 and l[j]>v:
            l[j+g]=l[j]
            j=j-g
            cnt+=1
        l[j+g]=v
    return l,cnt

def SP(l):
    for i in range(len(l)):
        if i !=len(l)-1:
            print(l[i],end=' ')
        else:
            print(l[i]) 

def shellSort(l,n):
    cnt=0
    G=[1]
    while True:
        if G[-1]*3+1<=n:
            G.append(G[-1]*3+1)
        else:
            G.reverse()
            break
    print(len(G))
    SP(G)
    for i in G:
        l,c=insertionSort(l,n,i)
        cnt+=c
    print(cnt)
    for i in l:
        print(i)

shellSort(a,n)
