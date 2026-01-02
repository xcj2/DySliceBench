CHANGE_COUNT = 0

def print_output(_list):
    for index in range(len(_list)):
        if index == len(_list) - 1:
            print(_list[index])
        else:
            print(_list[index],end=' ')

def insertion(target_list, g=1):
    global CHANGE_COUNT
    target_length = len(target_list)
    for index in range(g, target_length):
        v = target_list[index]
        j = index - g
        while (j >= 0 and target_list[j] > v):
            target_list[j + g] = target_list[j]
            j -= g
            CHANGE_COUNT += 1
        target_list[j + g] = v
    return target_list

def shellsort(target_list, shell_list):
    shell_length = len(shell_list)
    for shell_index in shell_list:
        target_list = insertion(target_list, shell_index)
    return target_list

target_list = [int(input()) for i in range(int(input()))]
target_length = len(target_list)
shell_list = []
shell_value = 1
while shell_value <= target_length:
    shell_list.append(shell_value)
    shell_value = 3 * shell_value + 1
shell_list.reverse()
print()
print(len(shell_list))
print_output(shell_list)
shellsort_list = shellsort(target_list, shell_list)
print(CHANGE_COUNT)
for shellsort_value in shellsort_list:
    print(shellsort_value)
