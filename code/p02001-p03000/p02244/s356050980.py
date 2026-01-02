def printBorad():
    for i in range(8):
        s = ['.'] * 8
        s[row[i]] = 'Q'
        print(''.join(s))

def putQueen(i, j):
    row[i] = j
    col[j] = True
    left[i+j] = True
    right[7+i-j] = True

def removeQueen(i, j):
    row[i] = False
    col[j] = False
    left[i+j] = False
    right[7+i-j] = False
    


def recursive(i):
    if i == 8:
        printBorad()
        return
    
    if row[i] is not False:
        putQueen(i, row[i])
        recursive(i + 1)
    else:
        for j in range(8):        
            if col[j] or left[i+j] or right[7+i-j]:
                continue
            putQueen(i, j)
            recursive(i + 1)
            removeQueen(i, j)


if __name__ == "__main__":
    row = [False for i in range(8)]
    col = [False for i in range(8)]
    left = [False for i in range(15)]
    right = [False for i in range(15)]
    n = int(input())
    for _ in range(n):
        i, j = map(int, input().split())
        putQueen(i, j)
    
    recursive(0)
