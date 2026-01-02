import sys

def swap(A, i, j):
    x = A[i]
    A[i] = A[j]
    A[j] = x

def partition(A, p, r, idx):
    x = A[r][idx]                # 1 x = A[r]
    i = p - 1                    # 2 i = p-1
    for j in range(p, r):        # 3 for j = p to r-1
        if A[j][idx] <= x:       # 4     if A[j] <= x
            i += 1               # 5        then i = i+1
            if(i != j):
                swap(A, i, j)    # 6        exchange A[i] and A[j] 
    i += 1 
    swap(A, i, r)                # 7 exchange A[i+1] and A[r]
    return i                     # 8 return i+1

def quickSort(A, p, r, idx):
    if p < r:
        q = partition(A, p, r, idx)
        quickSort(A, p, q - 1, idx)
        quickSort(A, q + 1, r, idx)

def main():
    """ ????????? """
    num = int(input().strip())
    istr = sys.stdin.read()
    cards = list(istr.splitlines())
    
    A = [[0,0] for i in range(num)]
    B = [[0,0] for i in range(num)]
    
    for i in range(num):
        A[i][0] = cards[i][0]
        A[i][1] = int(cards[i][2:])
        B[i][0] = cards[i][0]
        B[i][1] = int(cards[i][2:])

    quickSort(A, 0, num-1,1)
    B.sort(key = lambda d:d[1])
    res = "Stable"
    for i in range(num):
        if A[i][0] != B[i][0] or A[i][1] != B[i][1]:
            res = "Not stable"
            break

    print(res)
    for x in A:
        print(" ".join(map(str, x)))

if __name__ == '__main__':
    main()