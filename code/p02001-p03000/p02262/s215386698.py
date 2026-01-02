def insertion_sort(array, g):
    cnt = 0
    for i in range(g,len(array)):
        key = array[i]
        j = i - g
        while j >= 0 and array[j] > key:
            array[j+g] = array[j]
            j -= g
            cnt += 1
        array[j+g] = key
    return cnt

def shell_sort(array, ga):
    cnt = 0
    for g in ga:
        cnt += insertion_sort(array, g)
    return cnt

def print_array(array):
     print(str(array)[1:-1].replace(', ', ' '))


def main():
    N = int(input())
    array = [int(input()) for i in range(N)]
    # ga = [i for i in reversed(range(N)) if i % 3 == 1]
    ga = []
    v = 1
    while v <= N:
        ga.append(v)
        v = v * 3 + 1
    ga.reverse()
    cnt = shell_sort(array, ga)

    print(len(ga))
    print_array(ga)
    print(cnt)
    for v in array:
        print(v)

if __name__ == '__main__':
    main()