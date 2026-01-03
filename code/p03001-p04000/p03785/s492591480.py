import sys

def merge(L,R):
    res = []
    
    l_L = len(L)
    l_R = len(R)
    i = 0
    j = 0
    while (i <= l_L) & (j <= l_R):
        if (i == l_L) & (j == l_R):
            return res
        elif i == l_L:
            res.append(R[j])
            j += 1
        elif j == l_R:
            res.append(L[i])
            i += 1
        elif L[i] <= R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    return res

def divide(A):
    l_A = len(A)
    l_L = int(l_A / 2)
    l_R = l_A - l_L
    L = A[:l_L]
    R = A[l_L:]
    return L,R

def my_sort(A):
    l_A = len(A)
    if l_A == 1:
        return A
    else:
        L,R = divide(A)
        L = my_sort(L)
        R = my_sort(R)
        return merge(L,R)
    
N , C, K = map(int,input().split())
T = []
for _ in range(0,N):
    T.append(int(input()))
T = my_sort(T)

bus = 0
t_0 = T[0]
t_B = T[0] + K
num = 0


i = 0
while i < len(T):
    t = T[i]
    dt = t - t_0
    if (dt <= K) & (float((num + 1)) / float(C) <= 1):
        num += 1
    else:
        if num != 0:
            #print(T[i-1])
            bus += 1
            t_0 = t
            num = 1
    i += 1
bus += 1
print(bus)