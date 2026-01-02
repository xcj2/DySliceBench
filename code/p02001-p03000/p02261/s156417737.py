# Problem - 安定なソート

def bubble_sort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j][1]<C[j-1][1]:
                tmp = C[j]
                C[j] = C[j-1]
                C[j-1] = tmp
    return C

def selection_sort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1]<C[minj][1]:
                minj = j
        if not minj==i:
            tmp = C[i]
            C[i] = C[minj]
            C[minj] = tmp
    return C

def stable_check(check_dic, ans_list):
    is_ok = True
    for a in ans_list:
        v = a[0]
        k = a[1]
        if check_dic[k][0]==v:
            check_dic[k].pop(0)
        else:
            is_ok = False
    return is_ok

# input
N = int(input())
cards = input().split()
check_dic = {}
check_dic_2 = {}
cards_1 = ['']*N
cards_2 = ['']*N
for i in range(N):
    # dictionaly create
    c_list = list(cards[i])
    if not c_list[1] in check_dic:
        check_dic[c_list[1]] = [c_list[0]]
        check_dic_2[c_list[1]] = [c_list[0]]
    else:
        check_dic[c_list[1]].append(c_list[0])
        check_dic_2[c_list[1]].append(c_list[0])
    cards_1[i] = cards[i]
    cards_2[i] = cards[i]

# bubble sort
ans = bubble_sort(cards_1, N)
is_stable = stable_check(check_dic, ans)
print(" ".join(list(map(str, ans))))
if is_stable:
    print("Stable")
else:
    print("Not stable")

# selection sort
ans = selection_sort(cards_2, N)
is_stable = stable_check(check_dic_2, ans)
print(" ".join(list(map(str, ans))))
if is_stable:
    print("Stable")
else:
    print("Not stable")

