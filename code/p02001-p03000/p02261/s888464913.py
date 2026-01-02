import copy

N = int(input())
C = input().split(' ')

def bubble_sort(bubble_C, N):
    for i in range(N):
        for j in range(i+1, N)[::-1]:
            if int(bubble_C[j][1]) < int(bubble_C[j-1][1]):
                tmp = bubble_C[j]
                bubble_C[j] = bubble_C[j-1]
                bubble_C[j-1] = tmp
    return bubble_C

def selection_sort(sel_C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(sel_C[j][1]) < int(sel_C[minj][1]):
                minj = j
        tmp = sel_C[i]
        sel_C[i] = sel_C[minj]
        sel_C[minj] = tmp
    return sel_C

def check_stable(C1, C2):
    C_order_table = {}
    sorted_C_order_table = {}
    for i in range(len(C1)):
        if C_order_table.get(C1[i][1]):
            C_order_table[C[i][1]] += C1[i][0]
        else:
            C_order_table[C1[i][1]] = C1[i][0]
        
        if sorted_C_order_table.get(C2[i][1]):
            sorted_C_order_table[C2[i][1]] += C2[i][0]
        else:
            sorted_C_order_table[C2[i][1]] = C2[i][0]
    
    is_stable = True
    for n in range(1, 10):
        if C_order_table.get(str(n)) != sorted_C_order_table.get(str(n)):
            is_stable = False
            break
    
    if is_stable:
        print('Stable')
    else:
        print('Not stable')

bubble_C = copy.copy(C)
sel_C = copy.copy(C)

sorted_C = bubble_sort(bubble_C, N)
print(" ".join(sorted_C))
check_stable(C, sorted_C)

sorted_C = selection_sort(sel_C, N)
print(" ".join(sorted_C))
check_stable(C, sorted_C)
