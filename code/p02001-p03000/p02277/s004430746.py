def InputData():
    
    sequence_len = int(input())
    sequence = [input().split(" ") for _ in range(sequence_len)]
    sequence_m = [(a[0], int(a[1])) for a in sequence]
    sequence_q = [(a[0], int(a[1])) for a in sequence]
    return sequence_len, sequence_m, sequence_q

def partition(sequence, p, r):
    x = sequence[r]
    i = p - 1
    for j in range(p, r):
        if sequence[j][1] <= x[1]:
            i += 1
            sequence[i], sequence[j]= sequence[j], sequence[i]
    
    sequence[i+1], sequence[r] = sequence[r], sequence[i+1]
    return i+1

def quickSort(sequence, p, r):
    if p < r:
        q = partition(sequence, p, r)
        quickSort(sequence, p, q-1)
        quickSort(sequence, q+1, r)

def merge(sequence, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    sequence_left = sequence[left:left + n1]
    sequence_right = sequence[mid:mid + n2]
    sequence_left.append([None, float('inf')])
    sequence_right.append([None, float('inf')])

    left_cnt = 0
    right_cnt = 0
    for i in range(left, right):
        if sequence_left[left_cnt][1] <= sequence_right[right_cnt][1]:
            sequence[i] = sequence_left[left_cnt]
            left_cnt += 1
        else:
            sequence[i] = sequence_right[right_cnt]
            right_cnt += 1

def mergeSort(sequence, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(sequence, left, mid)
        mergeSort(sequence, mid, right)
        merge(sequence, left, mid, right)

def PrintOut(sequence_m, sequence_q):
    if sequence_m == sequence_q:
        print("Stable")
    else:
        print("Not stable")
    
    for a in sequence_q:
        print(a[0], a[1])

def main():
    [sequence_len, sequence_m, sequence_q] = InputData()
    mergeSort(sequence_m, 0, sequence_len)
    quickSort(sequence_q, 0, sequence_len-1)
    
    PrintOut(sequence_m, sequence_q)

if __name__=="__main__":
    main()
