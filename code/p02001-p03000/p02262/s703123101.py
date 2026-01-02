from copy import deepcopy

def getInput():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    return n, a

def insertionSort(n, a, g):
    cnt = 0
    for i in range(n):
        v = a[i]
        j = i-g
        while((j>=0)&(v<a[j])):
            a[j+g] = a[j]
            j -= g
            cnt += 1
        a[j+g] = v
    return a, cnt

def genG(n):
    G = []
    i = 0
    while 3*i+1 <= n:
        i = 3*i+1
        G.append(i)
    return G[::-1]

def shellSort(n, a):
    G = genG(n)
    cnt = 0
    print(len(G))
    print(" ".join([str(i) for i in G]))
    for g in G:
        a, cnt_g = insertionSort(n, deepcopy(a), g)
        cnt += cnt_g
    print(cnt)
    return a

n, a = getInput()
a = shellSort(n, deepcopy(a))
for i in a:
    print(i)
