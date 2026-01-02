def insertion_sort(A):
    for i in range(1, len(A)):
        print(A)
        v = A[i]
        j = i - 1
        while (j >= 0) and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
    return A


def bubble_sort(A):
    cnt = 0
    flag = True
    while flag:
        flag = False
        for i in sorted(range(1, len(A)), reverse=True):
            if A[i] < A[i - 1]:
                cnt += 1
                tmp = A[i]
                A[i] = A[i - 1]
                A[i - 1] = tmp
                flag = True
    return A, cnt


def selection_sort(A):
    for i in range(len(A)):
        minj = i
        for j in range(i, len(A)):
            if A[j] < A[minj]:
                minj = j
        tmp = A[i]
        A[i] = A[minj]
        A[minj] = tmp
    return A


def insertion_sort_for_shell(A, g):
    cnt = 0
    for i in range(g, len(A)):
        v = A[i]
        j = i - g
        while (j >= 0) and (A[j] > v):
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v
    return A, cnt

def shell_sort(A):
    cnt = 0
    G = []
    g = 1
    while True:
        G.append(g)
        g = g *3 + 1
        if g > len(A):
            break
    G = sorted(G, reverse=True)
    for g in G:
        A, c = insertion_sort_for_shell(A, g)
        cnt += c
    return A, G, cnt


def print_shell_sort_result(A, G, cnt):
    print(len(G))
    print(' '.join(map(str, G)))
    print(cnt)
    [print(a) for a in A]

if __name__ == '__main__':
    N = int(input())
    A = [0] * N
    for i in range(N):
        A[i] = int(input())
    print_shell_sort_result(*shell_sort(A))