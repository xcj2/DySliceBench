#! python3
# stableSort.py - 安定的なソートを行っているかどうか判別するプログラム

# インプットの例
# 5
# H4 C9 S4 D2 C3

# コマンド引数から値を受け取る
number = int(input())
array = input().split(' ')
bubble_array = array.copy()
select_array = array.copy()

# bubblesortのアルゴリズム
def bubbleSort(array, number):
    flag = 1
    i = 0
    while flag ==1:
        flag = 0
        for j in range(number-1, i, -1):
            if array[j][1] < array[j-1][1]:
                tmp = array[j]
                array[j] = array[j-1]
                array[j-1] = tmp
                flag = 1
    map_list = map(str, array)
    a = ' '.join(map_list)
    print(a)
    return array

# 選択ソートのアルゴリズム
def selectionSort(array, number):
    # counter = 0
    for i in range(number-1):
        mini_j = i
        for j in range(i + 1, number):
            if int(array[mini_j][1]) > int(array[j][1]):
                mini_j = j

        #if int(array[i][1]) > int(array[mini_j][1]):
        v = array[i]
        array[i] = array[mini_j]
        array[mini_j] = v
            # counter += 1

    map_list = map(str, array)
    a = ' '.join(map_list)
    print(a)
    return array

# 安定ソートかどうかを判別する
def isStable(input, output):
    for i in range(0, number):
        for j in range(i+1, number):
            for a in range(0, number):
                for b in range(a+1, number):
                    if input[i][1] == input[j][1] and input[i] == output[b] and input[j] == output[a]:
                        return 'Not stable'
    return 'Stable'

input = array
output_bubble = bubbleSort(bubble_array, number)
# print(output_bubble)
print(isStable(input, output_bubble))

output_select = selectionSort(select_array, number)
# print(output_select)
print(isStable(input, output_select))
