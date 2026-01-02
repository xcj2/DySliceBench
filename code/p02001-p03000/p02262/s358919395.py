# coding: utf-8

cnt = 0
m = 0
G = []
A = []

def insertionSort(A, n, g):
    global cnt
    for i in range(g,n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v

def shellSort(A, n):
    global m
    h = 1
    m += 1
    G.append(h)
    for i in range(99):
        if 3*h + 1 > n:
            break
        m += 1
        h = 3*h + 1
        G.append(h)
    G.reverse()
    for i in range(0,m):
        insertionSort(A, n, G[i])

def printA(A, n):
    for i in range(n):
        print(A[i])

def printG(G, m):
    for i in range(m):
        print(G[i],end="")
        if i == m - 1:
            print()
        else:
            print(" ",end="")

n = int(input().rstrip())
for i in range(n):
    A.append(int(input().rstrip()))

shellSort(A, n)
print(m)
printG(G, m)
print(cnt)
printA(A,n)
