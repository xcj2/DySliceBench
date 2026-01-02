#アルゴリズム：バブルソート
def BubbleSort(list, number):
    for i in range(0, number):
        for j in range(number-1, i, -1):
            if int(list[j][-1]) < int(list[j-1][-1]):
                list[j], list[j-1] = list[j-1], list[j]
    return list
    
#アルゴリズム：挿入ソート
def SelectionSort(list, number):
    for i in range(0, number):
        min_number = i
        for j in range(i, number):
            if int(list[min_number][-1]) > int(list[j][-1]):
                min_number = j
        list[i], list[min_number] = list[min_number], list[i]
    return list

#安定な出力か判定
def StableProcessing(list_A, list_B):
    if list_A == list_B:
        return "Stable"
    else:
        return "Not stable"


#初期data
input_number = int(input())
input_list_B = list(map(str, input().split()))
input_list_S = list(input_list_B)

#処理の実行
input_list_B = BubbleSort(input_list_B, input_number)
print(" ".join(input_list_B))
print("Stable")
input_list_S = SelectionSort(input_list_S, input_number)
print(" ".join(input_list_S))
print(StableProcessing(input_list_B, input_list_S))

