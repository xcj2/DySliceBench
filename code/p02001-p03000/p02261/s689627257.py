def bubbleSort(numlist):
    n = len(numlist)
    flag = True
    for i in range(n):
        if flag is False:
            break
        flag = False
        for j in range(n - 1, i, -1):
            if numlist[j][1] < numlist[j - 1][1]:
                numlist[j], numlist[j - 1] = numlist[j - 1], numlist[j]
                flag = True

def selectionSort(numlist):
    n = len(numlist)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numlist[min_index][1] > numlist[j][1]:
                min_index = j
        
        if min_index != i:
            numlist[min_index], numlist[i] = numlist[i], numlist[min_index]

def print_numlist(numlist):
    if len(numlist) == 1:
        print(numlist[0])
    else:
        n = len(numlist)
        for i in range(n - 1):
            print(numlist[i], end=' ')
        print(numlist[-1])

if __name__ == '__main__':
    n = int(input())
    numlist = [num for num in input().replace('\n', '').split(' ')]
    numlist2 = numlist.copy()
    bubbleSort(numlist)
    print_numlist(numlist)
    print('Stable')
    selectionSort(numlist2)
    print_numlist(numlist2)
    flag = True
    for i in range(len(numlist)):
        if numlist[i] != numlist2[i]:
            flag = False
            break
    if flag:
        print('Stable')
    else:
        print('Not stable')
