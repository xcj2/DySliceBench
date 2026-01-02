cnt = 0
def InsertionSort(A, n, g):
    global cnt

    for i in range(g, n):
        v = A[i]
        j = i - g

        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        
        A[j + g] = v

def ShellSort(A, n):
    G = list()
    gn = 1 

    while gn <= n:
        G.append(gn)
        gn = 3 * gn + 1

    m = len(G)
    G.reverse()

    for g in G:
        InsertionSort(A, len(A), g)

    return G

def Main():
    N = int(input())
    A = list()

    for n in range(N):
        A.append(int(input()))

    G = ShellSort(A, len(A))

    print(len(G))
    print(*G)
    print(cnt)
    print("\n".join(map(str, A)))

Main()
