global input_n
global input_data
global result

#インプットdata
input_n = int(input())
input_data = list(map(int, input().split()))
result = 0

#バブルソートプログラム
def bubbleSort():
    global result
    for i in range(input_n):
        jude = result
        for j in range(input_n-1, i, -1):
            if input_data[j] < input_data[j-1]:
                input_data[j], input_data[j-1] = input_data[j-1], input_data[j]
                result += 1
        if jude == result: break

#アルゴリズム：ソート
def merge(left, mid, right):
    global result
    
    n1 = mid - left
    n2 = right - mid
    inf = 10**9
    L_list = input_data[left: mid] + [inf]
    R_list = input_data[mid: right] + [inf]

    i = 0
    j = 0
    for k in range(left, right):
        if L_list[i] <= R_list[j]:
            input_data[k] = L_list[i]
            i += 1
        else:
            input_data[k] = R_list[j]
            j += 1
            result += n1 - i

#アルゴリズム：マージソート
def mergeSort(left, right):
    if (left + 1) < right:
        mid = (left + right) // 2
        mergeSort(left, mid)
        mergeSort(mid, right)
        merge(left, mid, right)

#処理の実行
#bubbleSort()
mergeSort(0, input_n)
print(result)
