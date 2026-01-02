from sys import stdin


def bubble_sort(A, N):
    for i in range(N-1):
        for j in range(N-1,0,-1):
            if int(A[j-1][1]) > int(A[j][1]):
                A[j], A[j-1] = A[j-1], A[j]
    return 'Stable'
                
def selection_sort(A, N, B):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        A[i], A[minj] = A[minj], A[i]


    if A == B:
        return 'Stable'
    else:
        return 'Not stable'

    
def main():
    read = stdin.readline
    N = int(read())
    data_for_bubble = list(map(str, read().split('\n')[0].split(' ')))
    data_for_selection = data_for_bubble.copy()
    bubble_result = bubble_sort(data_for_bubble, N)
    for i in range(N-1):
        print(data_for_bubble[i], end = ' ')
    print(data_for_bubble[N-1])
    print(bubble_result)
    selection_result = selection_sort(data_for_selection, N, data_for_bubble)
    for i in range(N-1):
        print(data_for_selection[i], end = ' ')
    print(data_for_selection[N-1])
    print(selection_result)
    
    
if __name__ == '__main__':
    main()
