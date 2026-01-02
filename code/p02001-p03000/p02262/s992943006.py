def show (nums):
    for i in range(len(nums)):
        if i!=len(nums)-1:
            print(nums[i],end=' ')
        else:
            print(nums[i])

def insertionSort(A,n,g):
    global cnt
    for i in range(g,n):
        v = A[i]
        j = i - g
        while(j >= 0 and A[j] > v):
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v

def shellSort(A,n):
    global cnt
    cnt = 0
    g = []
    h = 1
    while h <= n:
        g.append(h)
        h = 3*h+1
    g.reverse()
    m = len(g)
    for i in range(0,m):
        insertionSort(A,n,g[i])

    #出力
    print(m)
    show(g)
    print(cnt)
    for i in range(n):
        print(A[i])

#main
n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

shellSort(A,n)


