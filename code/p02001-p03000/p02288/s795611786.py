def parent(i):
    return(i // 2)

def left(i):
    return(i * 2)

def right(i):
    return(i * 2 + 1)

def maxHeapify(i):
    l = left(i)
    r = right(i)
    largest = 0
    
    if l <= H and A_list[l] > A_list[i]:
        largest = l
    else:
        largest = i
        
    if r <= H and A_list[r] > A_list[largest]:
        largest = r
    
    if largest != i:
        tmp_val = A_list[largest]
        A_list[largest] = A_list[i]
        A_list[i] = tmp_val
        maxHeapify(largest)

H = int(input())
A_list = list(map(int, input().split()))
A_list.insert(0, 0)
for i in range(H // 2, 0, -1):
    # print(i)
    # print(A_list)
    maxHeapify(i)
for i in range(1, H+1):
    print(" ", A_list[i], sep="", end="")
print("")
