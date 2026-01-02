def readinput():
    h=int(input())
    a=list(map(int,input().split()))
    a.insert(0,-1)
    return h,a

def maxHeapify(a,i):
    h=len(a)-1
    l=i*2
    r=i*2+1
    if (l<=h) and (a[l]>a[i]):
        largest=l
    else:
        largest=i
    if (r<=h) and (a[r]>a[largest]):
        largest=r
    
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(a,largest)

def buildHeap(a):
    h=len(a)-1
    for i in range(h//2, 0, -1):
        maxHeapify(a,i)


def main(h,a):
    buildHeap(a)
    return a

if __name__=='__main__':
    h,a=readinput()
    ans=main(h,a)
    print(' ',end=''); print(' '.join(map(str,a[1:])))
