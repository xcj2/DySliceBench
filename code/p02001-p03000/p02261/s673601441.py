def selection(n, data):
    __count = 0
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if data[min_i][1] > data[j][1]:
                min_i = j
        tmp = data[i]
        data[i] = data[min_i]
        data[min_i] = tmp
        if min_i != i:
            __count += 1
    return data, __count

def bubble_sort(n, data):
    __count = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j][1] > data[j+1][1]:
                tmp = data[j+1]
                data[j+1] = data[j]
                data[j] = tmp
                __count += 1
    return data, __count

def show(data):
    for i in range(len(data)):
        if i != (len(data)-1):
            print(data[i], end = " ")
        else:
            print(data[i])

if "__main__" == __name__:
    n = int(input())
    data_b = input().split()
    data_s = data_b.copy()
    sort1, count = bubble_sort(n, data_b)
    show(sort1)
    print("Stable")
    sort2, count = selection(n, data_s)
    show(sort2)
    if sort1 == sort2:
        print("Stable")
    else:
        print("Not stable")

