N = int(input())

A_list = list( map(int, input().split() ) )
B_list = list( map(int, input().split() ) )
C_list = list( map(int, input().split() ) )
# print(d,n,m)
# print(A_list)
# print(B_list)
# print(C_list)

A_sort = sorted(A_list)
C_sort = sorted(C_list)

# print("A:", A_sort)
# print("C:", C_sort)

def is_ok_lower(list_data, index: int, key: int):
    if (list_data[index] >= key):
        return True
    else:
        return False

def is_ok_upper(list_data, index: int, key: int):
    if (list_data[index] > key):
        return True
    else:
        return False


def binary_search(list_data, key: int, is_ok_func):
    ng = -1  #「index = 0」が条件を満たすこともあるので、初期値は -1
    ok = len(list_data) # 「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

    # どんな二分探索でもここの書き方を変えずにできる！
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2

        if (is_ok_func(list_data, mid, key)):
            ok = mid
        else:
            ng = mid

    # left は条件を満たさない最大の値、ok は条件を満たす最小の値になっている
    return ok

sum_conbi = 0
for B in B_list:
    a_key = binary_search(A_sort, B, is_ok_lower)
    c_key = binary_search(C_sort, B, is_ok_upper)

    # print(a_key, N-c_key)
    # print(B,">", A_sort[:a_key])
    # print(B,"<", C_sort[c_key:])

    sum_conbi += (a_key) * (N-c_key)

print(sum_conbi)
