def selection_sort(array):
    count_swap = 0
    for i in range(len(array)):
        minj = i
        for j in range(i + 1,len(array)):
            if num(array[j]) < num(array[minj]):
                minj = j
        if num(array[minj]) is not num(array[i]):
            tmp = array[minj]
            array[minj] = array[i]
            array[i] = tmp
            count_swap += 1
    return count_swap

def bubble_sort(array):
    isEnd = False
    count_swap = 0
    while isEnd is False:
        isEnd = True
        for j in reversed(range(1,len(array))):
            if num(array[j - 1]) > num(array[j]):
                tmp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = tmp
                count_swap += 1
                isEnd = False
    return count_swap

def print_array(array):
     print(str(array)[1:-1].replace(', ', ' ').replace('\'', ''))

def num(s):
    # print(s[1])
    return int(s[1])

def main():
    N = int(input())
    array = [s for s in input().split(' ')]
    array2 = [i for i in array]
    # print(array)
    bubble_sort(array)
    print_array(array)
    print('Stable')
    selection_sort(array2)
    print_array(array2)
    if array == array2:
        print('Stable')
    else:
        print('Not stable')

if __name__ == '__main__':
    main()