answer_printed = 0
answer=[]
for i in range(8):
    answer.append([])
for i in range(8):
    for j in range(8):
        answer[i].append('.')
row=[]
for i in range(8):
    row.append('.')
col=[]
for i in range(8):
    col.append('.')
right_slope=[]
for i in range(15):
    right_slope.append('.')
left_slope=[]
for i in range(15):
    left_slope.append('.')

def slope_change_r(x,y):
    return (x+y)%15

def slope_change_l(x,y):
    return (x-y+15)%15

def eightqueen(x,y,c):
    global answer_printed
    if c == 8:
        if answer_printed == 0:
            print_answer()
            answer_printed = 1
        return
    if x >= 8:
        return
    if row[x] == 'Q':
        if x<7:
            eightqueen(x+1,0,c)
        else:
            return
    for y in range(8):
        if is_all_clear(x,y):
            mark(x,y)
            eightqueen(x+1,0,c+1)
            unmark(x,y)

def mark(x,y):
    answer[x][y] = 'Q'
    row[x] = 'Q'
    col[y] = 'Q'
    right_slope[slope_change_r(x,y)] = 'Q'
    left_slope[slope_change_l(x,y)] = 'Q'

def unmark(x,y):
    answer[x][y] = '.'
    row[x] = '.'
    col[y] = '.'
    right_slope[slope_change_r(x,y)] = '.'
    left_slope[slope_change_l(x,y)] = '.'

def is_all_clear(x,y):
    if answer[x][y] == 'Q':
        return False
    if row[x] == 'Q':
        return False
    if col[y] == 'Q':
        return False
    if right_slope[slope_change_r(x,y)] == 'Q':
        return False
    if left_slope[slope_change_l(x,y)] == 'Q':
        return False
    return True

def print_answer():
    for i in range(8):
        for j in range(8):
            if answer[i][j] == 'Q':
                print('Q',end='')
            else:
                print('.',end='')
        print('',end='\n')
    
k = int(input())
while True:
    try:
        r,c = map(int,input().split())
    except:
            break
    else:
        mark(r,c)

eightqueen(0,0,k)


