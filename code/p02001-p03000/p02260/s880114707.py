def selection_sort(array):
    count_swap = 0
    for i in range(len(array)):
        minj = i
        for j in range(i + 1,len(array)):
            if array[j] < array[minj]:
                minj = j
        if array[minj] is not array[i]:
            tmp = array[minj]
            array[minj] = array[i]
            array[i] = tmp
            count_swap += 1
    return count_swap


def print_array(array):
     print(str(array)[1:-1].replace(', ', ' '))


def main():
    N = int(input())
    array = [int(s) for s in input().split(' ')]
    count = selection_sort(array)
    print_array(array)
    print(count)

if __name__ == '__main__':
    main()