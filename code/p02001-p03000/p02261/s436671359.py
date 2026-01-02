def get_value(s):
    return int(s[1])

def get_suit(s):
    return s[0]

def bubble_sort(A):
    a = list(A)
    for i in range(0, len(a)):
        
        
        for j in range(len(a)-1, i, -1):
            if get_value(a[j-1]) > get_value(a[j]):
                a[j-1], a[j] = a[j], a[j-1]
    return a

def selection_sort(A):
    a = list(A)
    for i in range(len(A)-1):
        i_min = i
        for j in range(i+1, len(A)):
            if get_value(a[j]) < get_value(a[i_min]):
                i_min = j
        a[i], a[i_min] = a[i_min], a[i]
    return a

def is_stable(A_orig, A_sort):
    dict_orig = {}
    dict_sort = {}
    
    # dict初期化
    for i in range(10):
        dict_orig[i] = list()
        dict_sort[i] = list()
    
    # dictに値設定
    for i in range(0, len(A_orig)):
        
        vo = get_value(A_orig[i])
        vs = get_value(A_sort[i])
        so = get_suit(A_orig[i])
        ss = get_suit(A_sort[i])
        
        dict_orig[vo].append(so)
        dict_sort[vs].append(ss)
    
    # stableかどうか検証
    for i in range(10):
        for j in range(len(dict_orig[i])):
            if dict_orig[i][j] is not dict_sort[i][j]:
                return False
    return True

input()
input_arr = input().split()

arr_bubble = bubble_sort(input_arr)
arr_selection = selection_sort(input_arr)

print(' '.join(arr_bubble))
print('Stable' if is_stable(input_arr, arr_bubble) else 'Not stable')
print(' '.join(arr_selection))
print('Stable' if is_stable(input_arr, arr_selection) else 'Not stable')
