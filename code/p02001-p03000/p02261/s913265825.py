def ssort(L, n):
    L = L[:]
    for i in range(n):
        minj = i
        for j in range(i, n):
            if L[j][1] < L[minj][1]:
                minj = j
        L[i], L[minj] = L[minj], L[i]
    return L

def bsort(L, n):
    L = L[:]
    for _ in L:
        for j in range(n-1, 0, -1):
            if L[j][1] < L[j-1][1]:
                L[j], L[j-1] = L[j-1], L[j]
    return L

def is_stable(L_in, L_out):
    in_pair_list= []
    out_pair_list= []
    for i, e1 in enumerate(L_in):
        for j, e2 in enumerate(L_in[i+1:]):
            if e1[1] == e2[1]:
                in_pair_list.append((e1, e2))
    for i, e1 in enumerate(L_out):
        for j, e2 in enumerate(L_out[i+1:]):
            if e1[1] == e2[1]:
                out_pair_list.append((e1, e2))
    return not bool(set(in_pair_list) - set(out_pair_list))

def print_stable(b):
    print('Stable' if b else 'Not stable')

n = int(input())
L = input().split()

b = bsort(L, n)
print(*b)
print_stable(is_stable(L, b))
s = ssort(L, n)
print(*s)
print_stable(is_stable(L, s))