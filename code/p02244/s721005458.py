N = 8
flag_row = [False]*N
flag_col = [False]*N
flag_diag_right = [False]*(2*N-1)
flag_diag_left  = [False]*(2*N-1)
B = [ [False for n in range(N)] for n in range(N)]

def ShowBoard():
    for i in range(N):
        for j in range(N):
            if B[i][j] :
                if flag_row[i] != j:
                    return

    for i in range(N):
        for j in range(N):
            if flag_row[i] == j:
                print("Q", end = "")
            else:
                print(".", end = "")
        print()

def SetQueen(i):
    if i == N  :
        ShowBoard()
        return

    for j in range(N):
        if flag_col[j] == False and flag_diag_left[i + j] == False and flag_diag_right[i - j + (N -1)] == False :

            flag_row[i] = j
            flag_col[j] = True
            flag_diag_left[i + j] = True
            flag_diag_right[i - j + (N -1)] = True

            SetQueen(i + 1)

            flag_row[i] = False
            flag_col[j] = False
            flag_diag_left[i + j] = False
            flag_diag_right[i - j + (N -1)] = False

def Main():
    K = int(input())

    for k in range(K):
        r, c = map(int, input().split())
        B[r][c] = True

    SetQueen(0)

Main()
