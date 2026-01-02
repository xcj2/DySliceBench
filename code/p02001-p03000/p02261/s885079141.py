import copy
def bs(array):
    for i in range(len(array)-1):
        for c in range(len(array)-1, i,-1):
            if array[c][1] < array[c-1][1]:
                swap = array[c]
                array[c] = array[c-1]
                array[c-1] = swap
    return array
def ss(array):
    for i in range(len(array)):
        minj = i
        for c in range(i+1,len(array)):
            if array[minj][1] > array[c][1]:
                minj = c
        swap = array[i]
        array[i] = array[minj]
        array[minj] = swap
    return array
def isStable(ar1,ar2):
    flag = 0
    for (x,y) in zip(ar1,ar2):
        if x != y:
            flag = 1
            break
    if flag == 0:
        print('Stable')
    else:
        print('Not stable')


n = input()
arr = [[i[0],int(i[1])] for i in input().split()]
arr1 = copy.deepcopy(arr)
arr2 = copy.deepcopy(arr)

bsarr = bs(arr2)
ssarr = ss(arr1)
print(' '.join([''.join([ x[0], str(x[1]) ]) for x in bsarr]))
print('Stable')
print(' '.join([''.join([ x[0], str(x[1]) ]) for x in ssarr]))
isStable(bsarr,ssarr)