def isOK_under(array, index, key):
    if array[index] >= key:
        return True
    else:
        return False

def isOK_over(array, index, key):
    if array[index] > key:
        return True
    else:
        return False

def binary_serch_under(array, key):
    ng = -1
    ok = len(array)

    while (abs(ok - ng) > 1):
        mid = (ok + ng)//2

        if isOK_under(array, mid, key):
            ok = mid
        else:
            ng = mid
    return ok

def binary_serch_over(array, key):
    ng = -1
    ok = len(array)
    while (abs(ok - ng) > 1):
        mid = (ok + ng)//2
        if isOK_over(array, mid, key):
            ok = mid
        else:
            ng = mid
    return ok

n = int(input())
array1 = list(map(int,input().split()))
array2 = list(map(int,input().split()))
array3 = list(map(int,input().split()))

array1 = sorted(array1)
array2 = sorted(array2)
array3 = sorted(array3)

# a = binary_serch(array2, 5)
count=0
# for array1_index in range(n):
#     start_array2_index = binary_serch(array2, array1[array1_index])
#     # print(array1[array1_index])
#     for cor_array2_index in range(start_array2_index, n):
#         # print(array2[cor_array2_index])
#         start_array3_index = binary_serch(array3, array2[cor_array2_index])
#         # for k in range(start_array3_index,n):
#         #     print(array3)
#         count+=abs(start_array3_index - n)
for index_array2 in range(n):
    a = binary_serch_under(array1, array2[index_array2])
    c = binary_serch_over(array3, array2[index_array2])
    count += a*abs(c-n)
print(count)
