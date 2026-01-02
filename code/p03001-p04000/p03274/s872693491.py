import sys

def ans(index, array, k):
    r = right(index, array, k)
    l =  left(index, array, k)
    return min(r, l)


def right(index, array, k):
    start = max(index, k-1)
    count = sys.maxsize
    for i in range(start, min(len(array), k+index)):
        tmp = array[i]
        j = index - (k - (i - index + 1))
        tmp += array[i] - array[j]
        count = count if count < tmp else tmp

    if len(array) > (index + k - 1):
        count = count if count < array[index + k - 1] else array[index + k - 1]
    
    return count

def left(index, array, k):
    n = len(array)
    start = min(index, n - k + 1)
    count = sys.maxsize
    
    for i in range(max(0, start - k), start):
        tmp = -array[i]
        j = k + i - 1
        tmp += -array[i] + array[j]
        count = count if count < tmp else tmp

    if index >= k:
        count = count if count < -array[index-k] else -array[index-k]
    
    return count

n,k = map(int, input().split())

x = [int(i) for i in input().split()] 

index = n
for i in range(n):
    if x[i] >= 0:
        index = i
        break

print(ans(index, x, k))