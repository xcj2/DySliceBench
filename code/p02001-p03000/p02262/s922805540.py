def insertion_sort(A, N, exchange_cnt):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
            exchange_cnt += 1
        A[j + 1] = v
    return A, exchange_cnt

def shell_sort(A, N, G):
    exchange_cnt = 0
    for g in G:
        for i in range(g):
            A[i::g], exchange_cnt = insertion_sort(A[i::g], len(A[i::g]), exchange_cnt)
    return A, exchange_cnt
    

def determine_G(N):
    G = [1]
    for i in range(N):
        G.append(G[i]*3 + 1)
        if G[-1] >= N:
            del G[-1]
            break
    return G[::-1]

N = int(input().rstrip())

A = []
for n in range(N):
    A.append(int(input().rstrip()))

G = determine_G(N)

    
result = shell_sort(A, N, G)
print(len(G))
print(" ".join([str(g) for g in G]))
print(result[1])
for num in result[0]:
    print(num)
