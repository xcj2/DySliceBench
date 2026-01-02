from array import array

def readinput():
    n=int(input())
    a=array('L',list(map(int,input().split())))
    return n,a

count=0
def merge(a,left,mid,right):
    INFTY=10**9+1
    global count
    n1=mid-left
    n2=right-mid
    #L=[a[left+i] for i in range(n1)]
    L=a[left:mid]
    L.append(INFTY)

    #R=[a[mid+i] for i in range(n2)]
    R=a[mid:right]
    R.append(INFTY)

    i=0;j=0
    for k in range(left,right):
        if(L[i]<=R[j]):
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        count+=1
   

def mergeSort(a,left,right):
    if(left+1<right):
        mid=(left+right)//2
        mergeSort(a,left,mid)
        mergeSort(a,mid,right)
        merge(a,left,mid,right)
    return

def main(n,a):
    global count
    mergeSort(a,0,n)
    return a,count

if __name__=='__main__':
    n,a=readinput()
    a,count=main(n,a)
    print(' '.join(map(str,a)))
    print(count)
