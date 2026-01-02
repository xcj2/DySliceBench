from queue import Queue as q
from copy import deepcopy as cp

def l_move(data):
    global flag
    field,n,i,j = data[0],data[1],data[2],data[3]
    if j == 0 or field[i][j-1] == 1 or n == 0:
        return(None)
    while(j):
        if field[i][j-1] == 0:
            j -= 1
        elif field[i][j-1] == 3:
            flag = True
            print(11-n)
            return(None)
        else:
            nfield = field[:i] + [field[i][:j-1] + [0] + field[i][j:]] + field[i+1:]

            n -= 1
            return([nfield,n,i,j])
    return(None)

def u_move(data):
    global flag
    field,n,i,j = data[0],data[1],data[2],data[3]
    if i == 0 or field[i-1][j] == 1 or n == 0:
        return(None)
    while(i):
        if field[i-1][j] == 0:
            i -= 1
        elif field[i-1][j] == 3:
            flag = True
            print(11-n)
            return(None)
        else:
            nfield = field[:i-1] + [field[i-1][:j] + [0] + field[i-1][j+1:]] + field[i:]

            n -= 1
            return([nfield,n,i,j])
    return(None)

def r_move(data):
    global flag
    field,n,i,j = data[0],data[1],data[2],data[3]

    if j == y-1 or field[i][j+1] == 1 or n == 0:
        return(None)
    while(j < y-1):
        if field[i][j+1] == 0:
            j += 1
        elif field[i][j+1] == 3:
            flag = True
            print(11-n)
            return(None)
        else:
            nfield = field[:i] + [field[i][:j+1] + [0] + field[i][j+2:]] + field[i+1:]

            n -= 1
            return([nfield,n,i,j])
    return(None)

def d_move(data):
    global flag
    field,n,i,j = data[0],data[1],data[2],data[3]
    if i == x-1 or field[i+1][j] == 1 or n == 0:
        return(None)
    while(i < x-1):
        if field[i+1][j] == 0:
            i += 1
        elif field[i+1][j] == 3:
            flag = True
            print(11-n)
            return(None)
        else:
            nfield = field[:i+1] + [field[i+1][:j] + [0] + field[i+1][j+1:]] + field[i+2:]

            n -= 1
            return([nfield,n,i,j])
    return(None)

while(True):
    flag = False
    y,x = map(int,input().split())
    lis = q()
    if x == 0:
        break
    field = []
    for i in range(x):
        field.append(list(map(int, input().split())))
    for i in range(x):
        for j in range(y):
            if field[i][j] == 2:
                start_x, start_y = i,j
                field[i][j] = 0
    data = [field,10,start_x,start_y]
    lis.put(data)
    while(lis.qsize()):
        d = lis.get()
        tmp = l_move(d)
        if flag:
            break
        if tmp != None:
            lis.put(tmp)
        tmp = u_move(d)
        if flag:
            break
        if tmp != None:
            lis.put(tmp)
        tmp = d_move(d)
        if flag:
            break
        if tmp != None:

            lis.put(tmp)
        tmp = r_move(d)
        if flag:
            break
        if tmp != None:
            lis.put(tmp)

        
    if not flag:
        print(-1)

