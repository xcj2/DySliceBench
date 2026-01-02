def getInput():
    n = int(input())
    a = [int(i) for i in input().split(" ")]
    return n, a

def swap(x, y):
    v = x
    x = y
    y = v
    return x, y

def bubbleSort(n, a):
    cnt = 0
    for j in range(n):
        init = True
        for i in range(n-1, -1, -1):
            if init:
                init = False
                continue
            if a[i] > a[i+1]:
                a[i], a[i+1] = swap(a[i], a[i+1])
                cnt += 1
    print(" ".join([str(i) for i in a]))
    print(cnt)
    return

n, a = getInput()
bubbleSort(n, a)

