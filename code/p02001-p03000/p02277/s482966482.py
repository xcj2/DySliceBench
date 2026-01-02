def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i+1]
    A[i+1] = A[r]
    A[r] = tmp
    return i+1
def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)
def check_stable(C1, C2):
    C_order_table = {}
    sorted_C_order_table = {}
    for i in range(len(C1)):
        if C_order_table.get(C1[i][1]):
            C_order_table[C1[i][1]] += C1[i][0]
        else:
            C_order_table[C1[i][1]] = C1[i][0]
        
        if sorted_C_order_table.get(C2[i][1]):
            sorted_C_order_table[C2[i][1]] += C2[i][0]
        else:
            sorted_C_order_table[C2[i][1]] = C2[i][0]
    
    is_stable = True
    for key in C_order_table.keys():
        if C_order_table.get(key) != sorted_C_order_table.get(key):
            is_stable = False
            break
    
    if is_stable:
        print('Stable')
    else:
        print('Not stable')
n = int(input())
A = []
for i in range(n):
    c_and_num = input().split(' ')
    c = c_and_num[0]
    num = int(c_and_num[1])
    A.append((c, num))
original_A = A.copy()
quick_sort(A, 0, n-1)
check_stable(original_A, A)
for c, num in A:
    print(c, num)
