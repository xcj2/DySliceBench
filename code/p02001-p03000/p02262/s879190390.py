import sys


def print_A(A):
    for i in range(len(A)):
        sys.stdout.write(str(A[i]))
        if i!= len(A) -1:
            sys.stdout.write(' ')
    print()


def insertionSort(A,n,g):
    cnt = 0
    for i in range(g,n):
        v = A[i]
        j = i - g
        while (j>=0) and (A[j] > v):
            A[j + g] = A[j]
            j -= g
            cnt +=1
        A[j + g] = v
    return cnt

def shellSort(A,n,G):
    cnt = 0
    for i in range(len(G)):
        cnt += insertionSort(A,n,G[i])
    return cnt
        

def get_gap(n):
    G = []
    h = 1
    cnt = 1
    while h <= n:
        G.append(h)
        h = 3*h + 1
        cnt +=1
    if len(G) == 0: G.append(1)
    return list(reversed(G))


n = int(input())
A = [0] * n
for i in range(n):
    A[i] = int(input())
    
G = get_gap(n)
m = len(G)
cnt = shellSort(A,n,G)

print(m)
print_A(G)
print(cnt)
for i in range(n):
    print(A[i])
