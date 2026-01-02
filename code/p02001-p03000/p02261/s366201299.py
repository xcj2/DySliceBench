N = int(input())
str_input = list(input().split())
T1 = [(S[0],int(S[1])) for S in str_input]
T2 = [(S[0],int(S[1])) for S in str_input]

def bubble_sort(N,T):
    for i in range(N):
        flag = True
        while flag:
            flag = False
            for j in range(N-1, i, -1):
                if T[j][1] < T[j-1][1]:
                    tmp = T[j]
                    T[j] = T[j-1]
                    T[j-1] = tmp
                    flag = True
    return T

def selection_sort(N,T):
    for i in range(N):
        min_index = i
        for j in range(i, N):
            if (T[j][1] < T[min_index][1]):
                min_index = j
        if (min_index != i):
            tmp = T[i]
            T[i] = T[min_index]
            T[min_index] = tmp
    return T

def is_stable(bT, sT):
    for i, st in enumerate(sT):
        if(st[0] != bT[i][0]):
            return False
    return True

def print_trump(T):
    strT = ['{}{}'.format(t[0],t[1]) for t in T]
    print(str(strT).replace(',','').replace('[','').replace(']','').replace("'",''))
    
bT = bubble_sort(N, T1)
sT = selection_sort(N, T2)
print_trump(bT)
print('Stable')
print_trump(sT)
stability = 'Stable' if is_stable(bT,sT) else 'Not stable'
print(stability)
