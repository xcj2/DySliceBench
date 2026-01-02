#coding: utf-8

def print_list(X):
    first_flag = True
    for val in X:
        if first_flag:
            print_line = str(val)
            first_flag = False
        else:
            print_line = print_line + ' ' + str(val)
    print(print_line)


def insertion_sort(A, n, g):
    global counter
    for i in range(g, n):
        tmp_val = A[i]
        j = i - g
        #print("tmp_val:", tmp_val, "A:", *A)
        while (j >= 0) and (A[j] > tmp_val):
            A[j+g] = A[j]
            j -= g
            counter += 1
            #print("tmp_val:", tmp_val, "A:", *A)
        A[j+g] = tmp_val

def shell_sort(A, n):
    global counter
    G = [i for i in [262913, 65921, 16577, 4193, 1073, 281, 77, 13, 4, 1] if i <= n]
    m = len(G)
    for i in range(0, m):
        insertion_sort(A, n, G[i])
    print(m)
    print(*G)
    print(counter)
    for i in range(n):
        print(A[i])


n = int(input())
A = [int(input()) for x in range(n)]
counter = 0

shell_sort(A, n)