c = 0

def merge(a,l,m,r):
    global c
    n1 = m-l
    n2 = r-m
    L = a[l:m]
    R = a[m:r]
    L.append(1000000009)
    R.append(1000000009)
    i,j = 0,0
    for k in range(l,r):
        if L[i]<=R[j]:
            a[k] = L[i]
            i += 1
        else :
            a[k] = R[j]
            j += 1
        c+=1

def mergeSort(a,l,r):
    if l+1<r:
        m = (l+r)//2
        mergeSort(a,l,m)
        mergeSort(a,m,r)
        merge(a,l,m,r)

def main():
    n = int(input())
    a = list(map(int,input().split()))
    mergeSort(a,0,n)
    print (' '.join(map(str,a)))
    print (c)

if __name__ == '__main__':
    main()


