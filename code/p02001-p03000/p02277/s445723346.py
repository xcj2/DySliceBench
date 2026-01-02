n = int(input())
trump = []
for i in range(n):
    str, num = input().split()
    num = int(num)
    trump.append((str, num, i))

def partition(a, p, r):
    x = a[r-1][1]
    i = p-1
    for j in range(p,r-1):
        if a[j][1] <= x:
            i = i+1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r-1] = a[r-1], a[i+1]
    return i+1

def quick_sort(a, p, r):
    if(p < r):
        q = partition(a, p, r)
        quick_sort(a, p, q)
        quick_sort(a, q+1, r)

def isStable(a):
    for i in range(1,len(a)):
        if a[i-1][1] == a[i][1]:
            if a[i-1][2] > a[i][2]:
                return False
    return True


quick_sort(trump,0,n)
if(isStable(trump)):
    print('Stable')
else:
    print('Not stable')
for i in trump:
    print('{} {}'.format(i[0], i[1]))

