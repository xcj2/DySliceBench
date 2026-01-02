import copy

def bubble_sort(array):
    N = len(array)
    unsorted_num_exist = True
    for i in range(N):
        unsorted_num_exist = False
        for j in reversed(range(i, N - 1)):
            if array[j][1] > array[j + 1][1]:
                unsorted_num_exist = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not unsorted_num_exist:
            break

def selection_sort(array):
    N = len(array)
    for i in range(N):
        min_index = i
        for j in range(i, N):
            if array[j][1] < array[min_index][1]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
 

def putsarray(array):
    for i in range(len(array) - 1):
        print(array[i][0] + str(array[i][1]), end=' ')
    print(array[-1][0] + str(array[-1][1]))

def check_stable(origin, sorted):
    dict_origin = {}
    for e in origin:
        num = e[1]
        if num in dict_origin.keys():
            dict_origin[num].append(e[0])
        else:
            dict_origin[num] = [e[0]]
    dict_sorted = {}
    for e in sorted:
        num = e[1]
        if num in dict_sorted.keys():
            dict_sorted[num].append(e[0])
        else:
            dict_sorted[num] = [e[0]]
    
    return all(dict_origin[key] == dict_sorted[key] for key in dict_origin.keys())

if __name__ == "__main__":
    N = int(input())
    array = input().split()
    array = [[s[0], int(s[1])] for s in array]
    array2 = copy.deepcopy(array)
    array3 = copy.deepcopy(array)
    bubble_sort(array2)
    putsarray(array2)
    print("Stable" if check_stable(array, array2) else "Not stable")
    selection_sort(array3)
    putsarray(array3)
    print("Stable" if check_stable(array, array3) else "Not stable")
