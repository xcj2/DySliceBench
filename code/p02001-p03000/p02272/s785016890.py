import math

def InputData():
    
    sequence_len = int(input())
    sequence = list(map(int, input().split(" ")))

    return sequence_len, sequence

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
        merge_cnt += 1
        if sequence_left[left_cnt] <= sequence_right[right_cnt]:
            # print(sequence_left[left_cnt])
            sequence[i] = sequence_left[left_cnt]
            left_cnt += 1
        else:
            # print(sequence_right[right_cnt])
            sequence[i] = sequence_right[right_cnt]
            right_cnt += 1

def mergeSort(sequence, left, right):
    if left + 1 < right:
        # print(merge_cnt)
        mid = (left + right) // 2
        mergeSort(sequence, left, mid)
        mergeSort(sequence, mid, right)
        merge(sequence, left, mid, right)

def PrintOut(sequence, merge_cnt):
    print(' '.join( map(str, sequence)))
    print(merge_cnt)

def main():
    global merge_cnt
    [sequence_len, sequence] = InputData()
    merge_cnt = 0
    mergeSort(sequence, 0, sequence_len)
    PrintOut(sequence, merge_cnt)

if __name__=="__main__":
    main()


