def insertion_sort(A, N, g):
    cnt = 0
    for i in range(g,N):
        v = A[i]
        j = i-g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v
        # print(' '.join([str(s) for s in A]))
    return cnt

def shell_sort(A,N):
    j = 1
    m = 0
    cnt = 0
    G = []
    while j <= N:
        G.append(j)
        j = 3*j+1
        m += 1
    
    G = G[::-1]
    
    for g in G:
        cnt += insertion_sort(A, N, g)
    print(m)
    print(' '.join([str(g) for g in G]))
    print(cnt)
    print('\n'.join([str(s) for s in A]))

def solve():
    input_line = input()
    N = int(input_line)
    A = []
    for _ in range(N):
        A.append(int(input()))

    shell_sort(A, N)
    
solve()
