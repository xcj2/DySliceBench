import sys

def is_stable(in_data, out_data):
    len_data = len(in_data)

    for i in range(len_data):
        for j in range(i+1, len_data):
            for a in range(len_data):
                for b in range(a+1, len_data):
                    if in_data[i][1] == in_data[j][1] and\
                       in_data[i] == out_data[b] and\
                       in_data[j] == out_data[a]:
                        return False

    return True

def bubble_sort(data, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if data[j][1] < data[j-1][1]:
                data[j], data[j-1] = data[j-1], data[j]

def selection_sort(data, n):
    for i in range(n):
        minj = i                # ??¨?????????????????????????°??????¨??????
        for j in range(i, n):
            if data[j][1] < data[minj][1]:
                minj = j

        data[i], data[minj] = data[minj], data[i]

def main():
    n = int(sys.stdin.readline().strip())
    card1 = sys.stdin.readline().strip().split(' ')

    card2 = card1[::]
    bubble_sort(card2, n)
    print(' '.join(card2))
    
    if is_stable(card1, card2):
        print('Stable')
    else:
        print('Not stable')

    card2 = card1[::]
    selection_sort(card2, n)
    print(' '.join(card2))
    
    if is_stable(card1, card2):
        print('Stable')
    else:
        print('Not stable')

if __name__ == '__main__':
    main()
    