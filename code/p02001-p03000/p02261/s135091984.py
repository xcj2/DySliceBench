#judge stable or not stbale

def printout(array, n):
    output = ""
    for i in range(n - 1):
        output += str(array[i]) + " "
    output += str(array[N - 1])
    print(output)


def bubble_sort(array):
    for i in range(N):
        for j in reversed(range(i+1,N)):
            if (int(array[j-1][1]) > int(array[j][1])):
                #swap
                tmp = array[j]
                array[j] = array[j-1]
                array[j-1] = tmp
    return array


def linearsearch(subarray):
    # return index of minimum array element
    min = int(subarray[0][1])
    min_index = 0;
    for i in range(1,len(subarray)):
        if min > int(subarray[i][1]):
            min = int(subarray[i][1])
            min_index = i
    return min_index


def selection_sort(array):
    index,tmp = 0,0
    for i in range(N):
        index = linearsearch(array[i:]) + i

        if index != i:
            #swap
            tmp = array[index]
            array[index] = array[i]
            array[i] = tmp
    return array


N = int(input())
array = [i for i in input().split()]
array1 = bubble_sort(array[:])
array2 = selection_sort(array[:])
original_array = array[:]

printout(array1,N)
print("Stable")
printout(array2,N)
if array1 == array2:
    print("Stable")
else:
    print("Not stable")

