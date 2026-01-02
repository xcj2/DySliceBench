N = int(input())

board_size = 8
board = [[ '.' for _ in range(board_size)] for _ in range(board_size)]

def print_board(board):
    for bb in board:
        line = ""
        for b in bb:
            line = line + b
        print(line)

#print_board(board)

Q_list = list()
for _ in range(N):
 Q_list.append(tuple(map(int, input().split() )) )
#print(Q_list)

skip_raws = list()
for (r,c) in Q_list:
    board[r][c] = "Q"
    skip_raws.append(r)


def is_enable_put(r, c, board):
    ok = True
    
    for i in range(board_size):
        # horizontal search
        if board[r][i] == "Q" and i != c:
            ok = False
            break
        # vertical search
        if board[i][c] == "Q" and i != r:
            ok = False
            break
        #
        if i > 0:
            if r-i >= 0 and c-i >= 0 \
            and board[r-i][c-i] == "Q":
                ok = False
                break
            if i+r < board_size and i+c < board_size \
            and board[i+r][i+c] == "Q":
                ok = False
                break
            if r-i >= 0 and c+i < board_size \
            and board[r-i][c+i] == "Q":
                ok = False
                break
            if r+i < board_size and c-i >= 0 \
            and board[r+i][c-i] == "Q":
                ok = False
                break
    return ok

import copy
def queen(r, qboard):
    # print("---", r)
    # print_board(qboard)
    if r == board_size:
        print_board(qboard)
        return
    elif r in skip_raws:
        queen(r+1,qboard)
        return

    else:
        for c in range(board_size):
            if is_enable_put(r, c, qboard) == False: continue
            else:
                tmp_board = copy.deepcopy(qboard)
                tmp_board[r][c] = "Q"
                queen(r+1, tmp_board)

queen(0,board)

