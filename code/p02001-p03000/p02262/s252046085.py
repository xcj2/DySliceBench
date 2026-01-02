# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 16:53:19 2016

@author: Yasuhiro_2
"""

def checkSorted(A):
    check = True
    a = A[0]
    for e in A:
        if a > e:
            check = False
            break
        else:
            a = e
    return check
        

def insertionSort(A, n, g, cnt):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v
    return [cnt, A]

"""
def shellSort(A, n):
    cnt = 0
    m = 0
    G = []          
    while checkSorted(A) == False:
        g = 1
        for i in range(n):
            j = i
            tmp = g
            while j < n:
                if A[i] > A[j]:
                    g = j - i
                j += tmp
        G.append(g)
        m += 1
        A = insertionSort(A, n, g, cnt)
        cnt = A[0]
        A = A[1]
    if m == 0:
        m = 1
        G = [1]
    return [m, G, cnt, A]
"""
def shellSort(A, n):
    cnt = 0
    m = 1
    G = [1]
    while G[-1] < n:
        G.append(3*G[-1] + 1)
        m += 1
    if m > 1:
        G = G[:-1]
        G.reverse()
        m -= 1
    
    for g in G:
        A = insertionSort(A, n, g, cnt)
        cnt = A[0]
        A = A[1]

    return [m, G, cnt, A]

            

if __name__ == '__main__':   
    n = int(input())
    A = []
    for i in range(n):
        A.append(int(input()))
    results = shellSort(A, n)
    m = results[0]
    G = results[1]
    cnt = results[2]
    Ar = results[3]
    print(m)
    gs = ''
    for g in G:
        gs = gs + str(g) + ' '
    print(gs[:-1])
    print(cnt)
    for a in Ar:
        print(a)
