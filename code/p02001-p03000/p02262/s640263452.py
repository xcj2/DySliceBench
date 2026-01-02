count = 0
def insertsort(array):
    for i in range(1,len(array)):
        temp = array[i]
        j = i-1
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp
    return array

def __insertsort(array,h):
    global count
    for i in range(h,len(array)):
        #print(" ".join(list(map(str,array))))
        temp = array[i]
        j = i-h
        while j >= 0 and temp < array[j]:
            array[j+h] = array[j]
            j -= h
            count += 1
        array[j+h] = temp
    return array


def shellsort(array):
    h = []
    ret = len(array)-1
    for i in range(len(array)):
        if ret > 1:
            h.append(ret)
            ret =int(ret/3)
        else:
            h.append(1)
            break

    for k in h:
        array = __insertsort(array,k)
    return len(h),h,array

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

a,b,c = shellsort(array)
print(a)
print(" ".join(list(map(str,b))))
print(count)
for i in c:
    print(i)

