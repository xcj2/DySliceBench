def bubble_sort(C, key):
    n = len(C)
    flag = True
    i = 0
    while flag:
        flag = False
        for j in range(n - 1, i, -1):
            if key(C[j]) < key(C[j - 1]):
                C[j - 1], C[j] = C[j], C[j - 1]
                flag = True
        i += 1

def selection_sort(C, key):
    n = len(C)
    for i in range(n):
        minj = i
        for j in range(i, n):
            if key(C[j]) < key(C[minj]):
                minj = j
        if i != minj:
            C[i], C[minj] = C[minj], C[i]

def chk_stable(org_arr, sorted_arr):
    n = len(org_arr)

    org_num_cnt = {}
    for i in range(n):
        num = org_arr[i][1]
        if num in org_num_cnt:
            org_num_cnt[num].append(i)
        else:
            org_num_cnt[num] = [i]

    is_stable = True
    _j = 0
    for i in range(1, n):
        if _j > 0:
            _j -= 1
            continue

        if sorted_arr[i-1][1] == sorted_arr[i][1]:
            idx_list = org_num_cnt[sorted_arr[i][1]]
            for j in range(len(idx_list)):
                if org_arr[idx_list[j]][0] != sorted_arr[i-1+j][0]:
                    is_stable = False
                    break
            _j = len(idx_list)-1
        if not is_stable:
            break

    return is_stable

n = int(input())

A = input().split()
C1 = A[:]
C2 = A[:]

bubble_sort(C1, lambda x: x[1])
print(*C1)
if chk_stable(A, C1) == True:
    print("Stable")
else:
    print("Not stable")

selection_sort(C2, lambda x: x[1])
print(*C2)
if chk_stable(A, C2) == True:
    print("Stable")
else:
    print("Not stable")
