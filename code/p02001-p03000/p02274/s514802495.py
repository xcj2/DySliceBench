def InputData():
    
    sequence_len = int(input())
    sequence = [int(a) for a in input().split(" ")]

    return sequence_len, sequence

def bubbleSort(A):
    cnt = 0
    for i in range(len(A)-1):
        for j in range(len(A)-1, i+1, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                cnt += 1
    
    return cnt

def merge(sequence, left, mid, right):
    global merge_cnt
    n1 = mid - left
    n2 = right - mid
    sequence_left = sequence[left:left + n1]
    sequence_right = sequence[mid:mid + n2]
    sequence_left.append(float('inf'))
    sequence_right.append(float('inf'))

    left_cnt = 0
    right_cnt = 0
    for i in range(left, right):
        if sequence_left[left_cnt] <= sequence_right[right_cnt]:
            # print(sequence_left[left_cnt])
            sequence[i] = sequence_left[left_cnt]
            left_cnt += 1
        else:
            # print(sequence_right[right_cnt])
            sequence[i] = sequence_right[right_cnt]
            right_cnt += 1
            merge_cnt += n1 - left_cnt

def mergeSort(sequence, left, right):
    if left + 1 < right:
        # print(merge_cnt)
        mid = (left + right) // 2
        mergeSort(sequence, left, mid)
        mergeSort(sequence, mid, right)
        merge(sequence, left, mid, right)

def PrintOut(cnt):
    print(cnt)

def main():
    [sequence_len, sequence] = InputData()
    # cnt = bubbleSort(sequence)
    global merge_cnt
    merge_cnt = 0
    mergeSort(sequence, 0, sequence_len)
    PrintOut(merge_cnt)

if __name__=="__main__":
    main()
