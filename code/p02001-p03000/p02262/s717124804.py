# print(str(I).replace(',','').replace('[','').replace(']',''))

def insertion_sort(A, N, g):
    cnt = 0
    for i in range(g, N):
        v = A[i]
        j = i - g
        while (j >= 0 and A[j] > v):
            A[j+g] = A[j]
            j -= g 
            cnt += 1
        A[j+g] = v
    return cnt
    
def shell_sort(A, N, G):
    cnt = 0
    for i in range(len(G)):
        cnt += insertion_sort(A, N, G[i])
    return cnt

def calc_g(N):
    h = 1
    G = []
    while True:
        if (h > N):
            break
        G.insert(0,h)
        h = 3 * h + 1
    return G

N = int(input())
A = [int(input()) for _ in range(N)]
G = calc_g(N)

cnt = shell_sort(A, N, G)

print(len(G))
print(str(G).replace(',','').replace('[','').replace(']',''))
print(cnt)
[print(x) for x in A]
