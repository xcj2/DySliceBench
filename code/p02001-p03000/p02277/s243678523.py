def partition(a,p,r)->int:
    x = a[r][1]
    i = p-1
    for j in range(p,r):
        if a[j][1]<=x:
            i+=1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r],a[i+1]
    return i+1

def quick_sort(a,l,r):
    if l<r:
        q = partition(a,l,r)
        quick_sort(a,l,q-1)
        quick_sort(a,q+1,r)

def check(a):
    for i in range(len(a)):
        j = i+1
        while j<len(a) and a[i][1]==a[j][1]:
            if a[j][2]<a[i][2]:return 'Not stable'
            j+=1
    return 'Stable'

def main():
    n = int(input())
    a = []
    for i in range(n):
        b,c = input().split()
        a.append([b,int(c),i])
    quick_sort(a,0,n-1)
    print (check(a))
    for b,c,_ in a:print (b,c)

if __name__ == '__main__':
    main()


