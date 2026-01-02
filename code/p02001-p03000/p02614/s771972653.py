import copy

def find(h):
    bits_active = {}
    for i in range(pow(2,h)):
        x = bin(i)[2:]
        if len(x) < h:
            x = '0'*(h-len(x))+x

        ones = x.count('1')
        if ones not in bits_active.keys():
            bits_active[ones] = []

        bits_active[ones].append(x)

    return bits_active

def good(grid,h,w,row_perm,col_perm,k):
    temp = copy.deepcopy(grid)
    for i in range(h):
        if row_perm[i] == '1':
            for j in range(w):
                temp[i][j] = 'r'

    for j in range(w):
        if col_perm[j] == '1':
            for i in range(h):
                temp[i][j] = 'r'

    count = 0
    for i in range(h):
        for j in range(w):
            if temp[i][j] == '#':
                count += 1

    if count == k:
        return True

    return False

def main():
    h,w,k = map(int,input().split())
    grid = []
    for i in range(h):
        grid.append(list(input()))

    bits_active_rows = find(h)
    bits_active_cols = find(w)
    total = 0
        
    for rows_chosen in range(h+1):
        for cols_chosen in range(w+1):
            for row_perm in bits_active_rows[rows_chosen]:
                for col_perm in bits_active_cols[cols_chosen]:
                    if good(grid,h,w,row_perm,col_perm,k):
                        total += 1

    print(total)

main()
