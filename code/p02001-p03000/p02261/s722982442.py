#安定なソート判定
def print_output(_list):
    for index in range(len(_list)):
        if index == len(_list) - 1:
            print(_list[index])
        else:
            print(_list[index],end=' ')

def bubble(_target_list):
    target_list = _target_list.copy()
    for index in range(1, len(target_list)):
        for compare_index in reversed(range(index)):
            if target_list[compare_index + 1][1] < target_list[compare_index][1]:
                target_list[compare_index + 1] ,target_list[compare_index] = target_list[compare_index] ,target_list[compare_index + 1]
            else:            
                break
    return target_list

def selection(_target_list):
    target_list = _target_list.copy()
    for i in range(len(target_list)):
        minj = i
        for j in range(i, len(target_list)):
            if target_list[j][1] < target_list[minj][1]:
                minj = j
        if i != minj:
            target_list[i], target_list[minj] = target_list[minj], target_list[i]
    return target_list

target_length = int(input())
target_list = [x for x in input().split()]

bubble_list = bubble(target_list)
print_output(bubble_list)
print("Stable")
selection_list = selection(target_list)
print_output(selection_list)
if bubble_list == selection_list:
    print("Stable")
else:
    print("Not stable")
