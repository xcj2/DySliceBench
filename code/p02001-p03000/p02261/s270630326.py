def BubbleSort(C, N):
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if int(C[j][1]) < int(C[j-1][1]):
                C[j], C[j-1] = C[j-1], C[j]
    return C

def SelectionSort(C, N):
    for i in range(N):
        min_j = i
        for j in range(i+1, N):
            if int(C[j][1]) < int(C[min_j][1]):
                min_j = j
        C[i], C[min_j] = C[min_j], C[i] 
    return C

def isStable(in_list, out_list):
    N = len(in_list)
    for i_in in range(N):
        for j_in in range(i_in+1, N):
            for i_out in range(N):
                for j_out in range(i_out+1, N):
                    if (in_list[i_in][1] == in_list[j_in][1]) and\
                       (in_list[i_in] == out_list[j_out]) and\
                       (in_list[j_in] == out_list[i_out]):
                        return False
    return True

if __name__ == "__main__":
    N = int(input())
    C = list(map(str, input().split()))
    C1 = C.copy()
    C2 = C.copy()
    Bubble_C = BubbleSort(C1, N)
    Selection_C = SelectionSort(C2, N)

    print(*Bubble_C)
    print('Stable')
    print(*Selection_C)
    if Bubble_C == Selection_C:
        print('Stable')
    else:
        print('Not stable')
