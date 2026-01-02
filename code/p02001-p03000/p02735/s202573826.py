def inp(wide):
    a = input()
    ans = []
    for i in range(wide):
        if a[i] == '.':
            ans.append(['w',float('Inf')])
        else:
            ans.append(['b',float('Inf')])
    return ans
def chang(up,left,nex): 
    if nex[0] == 'w':
        return min(up[1],left[1])
    else:
        d = up[1]
        g = left[1]
        if up[0] == 'w':
            d = d+1
        if left[0] == 'w':
            g = g+1
        return min(d,g)
def main(board,high,wide,already):
    for i in range(wide):
        if 0 <= already-i and already -i < high:
            nex = board[already-i][i]
            if 0 <= already-i-1 and 0 <= i-1:
                board[already-i][i][1] = chang(board[already-i-1][i],board[already-i][i-1],nex)
            elif 0 <= already-i-1 and 0 > i-1:
                board[already-i][i][1] = chang(board[already-i-1][i],['w',float('inf')],nex)
            else:
                board[already-i][i][1] = chang(['w',float('inf')],board[already-i][i-1],nex)
    
    if already == high + wide -1:
        return board[high-1][wide-1][1]
    return main(board,high,wide,already+1)
    

a = input().split()
high = int(a[0])
wide = int(a[1])

board = []
for i in range(high):
    board.append([])
    board[i] = inp(wide)
if board[0][0][0] == 'w':
    board[0][0][1] = 0
else:
    board[0][0][1] = 1

if high < wide:
    bo = []
    for i in range(wide):
        bo.append([])
        for j in range(high):
            bo[i].append(board[j][i])   
else:
    bo = board
ans = main(bo,max(wide,high),min(wide,high),1)
print(ans)