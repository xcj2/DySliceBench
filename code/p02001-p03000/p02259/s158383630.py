def bubble_sort(array):
    isEnd = False
    count_swap = 0
    while isEnd is False:
        isEnd = True
        for j in reversed(range(1,len(array))):
            if array[j - 1] > array[j]:
                tmp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = tmp
                count_swap += 1
                isEnd = False
    return count_swap

def print_array(array):
     print(str(array)[1:-1].replace(', ', ' '))

def main():
    N = int(input())
    array = [int(s) for s in input().split(' ')]
    count = bubble_sort(array)
    print_array(array)
    print(count)

if __name__ == '__main__':
    main()