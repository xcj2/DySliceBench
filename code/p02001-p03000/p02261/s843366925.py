def isStable(before_sort, after_sort):
    num = len(before_sort)
    
    for i in range(0, num-1):
        for j in range(i+1, num):
            for a in range(0, num-1):
                for b in range(a+1, num):
                    if before_sort[i][1] == after_sort[j][1] and \
                       before_sort[i] == after_sort[b] and \
                       before_sort[j] == after_sort[a]:
                        return False
    return True

def isStable2(sorted_data, bubble_sort_data):
    for i in range(0, len(sorted_data)):
        if sorted_data[i] != bubble_sort_data[i]:
            return False
    return True
    
def BubbleSort(c, n):
    for i in range(0, n):
        for j in range(n-1, i, -1):
            if int(c[j][1]) < int(c[j-1][1]):
                c[j], c[j-1] = c[j-1], c[j]

def SelectionSort(c, n):
    for i in range(0, n):
        minj = i
        for j in range(i, n):
            if int(c[j][1]) < int(c[minj][1]):
                minj = j
        c[i], c[minj] = c[minj], c[i]
    
num = int(input())
data = input().split(' ')

copy_data = data.copy()
BubbleSort(copy_data, num)
print(' '.join(copy_data))
if isStable(copy_data, copy_data):
    print("Stable")
else:
    print("Not stable")

bubble_sort_data = data.copy()
SelectionSort(bubble_sort_data, num)
print(' '.join(bubble_sort_data))
if isStable(bubble_sort_data, copy_data):
    print("Stable")
else:
    print("Not stable")